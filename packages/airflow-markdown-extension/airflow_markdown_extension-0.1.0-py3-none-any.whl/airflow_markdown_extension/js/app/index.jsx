import React from 'react'
import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from "react-query";
import 'reactflow/dist/style.css';
import { BrowserRouter } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";
import moment from "moment-timezone";

import Graph from '../airflow/dag/details/graph/index.tsx'
import { ContainerRefProvider, useContainerRef } from "../airflow/context/containerRef";
import theme from "../airflow/theme";
import './index.css'


global.stateColors = {
  deferred: "mediumpurple",
  failed: "red",
  queued: "gray",
  removed: "lightgrey",
  restarting: "violet",
  running: "lime",
  scheduled: "tan",
  skipped: "hotpink",
  success: "green",
  up_for_reschedule: "turquoise",
  up_for_retry: "gold",
  upstream_failed: "orange",
};

global.defaultDagRunDisplayNumber = 245;

global.filtersOptions = {
  // Must stay in sync with airflow/www/static/js/types/index.ts
  dagStates: ["success", "running", "queued", "failed"],
  runTypes: ["manual", "backfill", "scheduled", "dataset_triggered"],
};

global.moment = moment;

global.standaloneDagProcessor = true;

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      notifyOnChangeProps: "tracked",
      refetchOnWindowFocus: false,
      retry: 1,
      retryDelay: 500,
      refetchOnMount: true, // Refetches stale queries, not "always"
      staleTime: 5 * 60 * 1000, // 5 minutes
      initialDataUpdatedAt: new Date().setMinutes(-6), // make sure initial data is already expired
    },
    mutations: {
      retry: 1,
      retryDelay: 500,
    },
  },
});

const voidReturn = (input) => {};

const InnerContainerRefWrapper = ({graph_data, dataset_data, grid_data}) => {
    const containerRef = useContainerRef();
    return (
        <ChakraProvider
          theme={theme}
          toastOptions={{ portalProps: { containerRef } }}
        >
            <QueryClientProvider client={queryClient}>
                <BrowserRouter>
                    <Graph
                        openGroupIds={[]}
                        onToggleGroups={voidReturn}
                        hoveredTaskState={null}
                        isFullScreen={false}
                        toggleFullScreen={voidReturn}
                        graph_data={graph_data}
                        dataset_data={dataset_data}
                        grid_data={grid_data}
                    />
                </BrowserRouter>
            </QueryClientProvider>
        </ChakraProvider>
    )
}

export function AirflowGraph(elementId, graph_data, dataset_data, grid_data) {
    const container = document.getElementById(elementId);
    ReactDOM.createRoot(container).render(
        <React.StrictMode>
            <ContainerRefProvider>
                <InnerContainerRefWrapper
                    graph_data={graph_data}
                    dataset_data={dataset_data}
                    grid_data={grid_data}
                />
            </ContainerRefProvider>
        </React.StrictMode>,
    )
}

window.AirflowGraph = AirflowGraph;