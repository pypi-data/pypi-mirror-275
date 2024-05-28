import csv
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import typer


@dataclass
class LineInfo:
    source_file_path: Path
    line_no: int
    scope: str
    key: str

    def key_has_str_interpolation(self) -> bool:
        # str interpolation are in the shape of ${xxx}
        return re.search(r"\${[^}]+}", self.key) is not None

    @classmethod
    def from_grep_line(cls, grep_line: str):
        source_file_path, line_no, key = grep_line.split(":", 2)
        source_file_path = Path(source_file_path)
        key = key.removeprefix("t(").removesuffix(")").strip("""'"`""")
        if ":" in key:
            scope, *key = key.split(":")
            key = ".".join(key)
        else:
            scope = "common"
        return cls(source_file_path, int(line_no), scope, key)


def extract_matched_lines(root_path: Path):
    cmd = [
        "find",
        str(root_path),
        "-name",
        "*.tsx",
        "-exec",
        "grep",
        # only matched line
        "-o",
        # word boundary
        "-w",
        # line number
        "-n",
        # match against t("key") / t('key') / t(`key`)
        "-E",
        r"""t\(("[^"]+"|'[^']+'|`[^`]+`)\)""",
        "{}",
        "+",
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode().splitlines()


def load_scope_key_file(f: typer.FileText) -> dict[str, dict[str, list[str]]]:
    reader = csv.DictReader(f, delimiter="\t")
    result = {}
    # group by scope and then key
    for row in reader:
        scope = row["scope"]
        key = row["key"]
        locales = row["locales"].split(",")
        result.setdefault(scope, {})[key] = locales
    return result


def init_count_dict(
    scope_key_dict: dict[str, dict[str, list[str]]],
) -> dict[str, dict[str, int]]:
    result = {}
    for scope, key_dict in scope_key_dict.items():
        result[scope] = {key: 0 for key in key_dict}
    return result
