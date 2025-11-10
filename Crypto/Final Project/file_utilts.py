import json

def load_data(file_name: str):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_data(data, file_name: str):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def start_files(file_names: list[str]):
    for file_name in file_names:
        try:
            with open(file_name, "r", encoding="utf-8"):
                pass
        except FileNotFoundError:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write("{}")