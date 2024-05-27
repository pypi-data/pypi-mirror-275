from __future__ import annotations

import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import flask
from airflow import Dataset
from airflow.api_connexion.schemas.dataset_schema import (
    dataset_collection_schema,
    DatasetCollection,
)
from airflow.datasets import DatasetAll
from airflow.models import DAG, DagBag
from airflow.models.dataset import DatasetModel
from airflow.utils.dag_edges import dag_edges
from airflow.utils.task_group import task_group_to_dict
from jinja2.utils import htmlsafe_json_dumps

from airflow_markdown_extension.utils import generate_random_string

if TYPE_CHECKING:
    import markdown


class DagParser:
    @staticmethod
    def _parse_dag(folder: str) -> DAG:
        """Parse and return the first dag loaded in a dag folder."""
        dag_bag = DagBag(dag_folder=folder, include_examples=False)
        return list(dag_bag.dags.values())[0]

    @staticmethod
    def _get_datasets(dag: DAG) -> list[DatasetModel]:
        """Get the datasets related to a dag."""
        trigger = dag.dataset_triggers
        if trigger is not None:
            if isinstance(trigger, Dataset):
                return [DatasetModel.from_public(trigger)]
            elif isinstance(trigger, DatasetAll):
                return [
                    DatasetModel.from_public(dataset) for dataset in trigger.objects
                ]
            else:
                raise NotImplemented(
                    f"Cannot extract Dataset data from '{type(trigger)}' object."
                )
        return []

    @classmethod
    def parse(cls, dag_folder: str) -> tuple[DAG, list[DatasetModel]]:
        dag = cls._parse_dag(folder=dag_folder)
        datasets = cls._get_datasets(dag=dag)
        return dag, datasets


# Source: https://github.com/apache/airflow/blob/main/airflow/www/views.py#L3174
def make_graph_data(dag: DAG) -> str:
    """Generate DAG graph data and return it as JSON."""
    nodes = task_group_to_dict(dag.task_group)
    edges = dag_edges(dag)

    data = {
        "arrange": dag.orientation,
        "nodes": nodes,
        "edges": edges,
    }
    return htmlsafe_json_dumps(obj=data, separators=(",", ":"), dumps=flask.json.dumps)


def make_dataset_data(datasets: list[DatasetModel]) -> str:
    """Generate Dataset data and return it as JSON."""
    data = DatasetCollection(datasets=datasets, total_entries=len(datasets))

    return htmlsafe_json_dumps(
        obj=dataset_collection_schema.dump(data),
        separators=(",", ":"),
        dumps=flask.json.dumps,
    )


def make_grid_data(dag: DAG):
    """Return grid data."""

    # TODO: implement support for nested task groups
    children = []
    for task_id, task in dag.task_dict.items():
        children.append(
            {
                "extra_links": task.extra_links,
                # TODO: Implement Dataset in outlets detection
                "has_outlet_datasets": bool(task.outlets),
                "id": task_id,
                "instances": [],
                # TODO: Implement mapped task support
                "is_mapped": False,
                "label": task.label,
                "operator": getattr(task, "custom_operator_name", task.task_id),
                "trigger_rule": str(task.trigger_rule),
            }
        )

    data = {
        "groups": {"children": children, "id": None, "instances": [], "label": None},
        "dag_runs": [],
        "ordering": dag.timetable.run_ordering,
    }
    return htmlsafe_json_dumps(obj=data, separators=(",", ":"), dumps=flask.json.dumps)


def fence_airflow_dag_format(
    source: str,
    language: str,
    css_class: str,
    options: dict,
    md: markdown.core.Markdown,
    **kwargs,
) -> str:
    """Format fence into a JSON representation of an Airflow DAG."""

    with tempfile.TemporaryDirectory() as temp_dir:
        with open(Path(temp_dir) / "dag.py", "w") as dag_file:
            dag_file.write(source)
        dag, datasets = DagParser.parse(temp_dir)

    graph_data = make_graph_data(dag=dag)
    dataset_data = make_dataset_data(datasets=datasets)
    grid_data = make_grid_data(dag=dag)

    div_id: str = generate_random_string()
    html_graph = f"""
        <div id="{div_id}"></div>
        <script type="module">
            const graph_data = {graph_data};
            const dataset_data = {dataset_data};
            const grid_data = {grid_data};
            window.AirflowGraph("{div_id}", graph_data, dataset_data, grid_data);
        </script>
        """
    return html_graph
