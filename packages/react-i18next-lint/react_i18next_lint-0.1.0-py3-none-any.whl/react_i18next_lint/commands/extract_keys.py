import json
from pathlib import Path
from typing import Generator


def flatten_keys_on_dict(
    data: dict, prefix=()
) -> Generator[tuple[str, str], None, None]:
    for key, value in data.items():
        key_path = prefix + (key,)
        if isinstance(value, dict):
            yield from flatten_keys_on_dict(value, prefix=key_path)
        else:
            yield ".".join(key_path), value


RESOURCES_TSV_KEY_SET = ("locale", "scope", "full_path", "key", "value")


def extract_keys_from_file(
    root_path: Path, json_file: Path
) -> Generator[dict[str, str], None, None]:
    locale, file_name = str(json_file.relative_to(root_path)).split("/")
    scope = file_name.removesuffix(".json")
    full_path = json_file.resolve()
    with json_file.open("r") as f:
        data = json.load(f)
        for key, value in flatten_keys_on_dict(data):
            row_data = (locale, scope, full_path, key, value)
            yield dict(zip(RESOURCES_TSV_KEY_SET, row_data))
