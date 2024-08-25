import json


def load_counts(pokemon: str) -> int:
    try:
        with open('counts.json', 'r') as f:
            json_data = json.load(f)
            return json_data[pokemon]
    except (KeyError, FileNotFoundError):
        return 0


def save_counts(pokemon: str, new_count: int) -> None:
    json_data = {}
    try:
        with open('counts.json', 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        pass

    json_data[pokemon] = new_count

    with open('counts.json', 'w') as f:
        json.dump(json_data, f)
