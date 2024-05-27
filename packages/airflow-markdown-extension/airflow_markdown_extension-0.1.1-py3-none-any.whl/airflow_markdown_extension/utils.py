import random
import string


def generate_random_string(length: int = 5) -> str:
    characters: str = string.ascii_lowercase + string.digits
    return "".join(random.choices(characters, k=length))
