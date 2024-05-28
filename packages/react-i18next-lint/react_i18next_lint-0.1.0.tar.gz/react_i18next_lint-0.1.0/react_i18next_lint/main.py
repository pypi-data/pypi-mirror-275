import csv
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from .commands.extract_keys import RESOURCES_TSV_KEY_SET, extract_keys_from_file
from .commands.group_key_locales import transform_resources_group_by_key
from .commands.validate_keys import (
    LineInfo,
    extract_matched_lines,
    init_count_dict,
    load_scope_key_file,
)

app = typer.Typer()


error_console = Console(stderr=True, style="bold red")


@app.command()
def group_key_locales(phrases_file: Path, output_path: Path):
    """
    Group the phrases tsv file extracted from the extract_key script as given by PHRASES_FILE,
    group by scope and key, and aggregate the locales, write out to OUTPUT_PATH as tsv file
    """
    assert phrases_file.exists(), f"{phrases_file} does not exist"
    assert phrases_file.is_file(), f"{phrases_file} is not a file"
    assert phrases_file.suffix == ".tsv", f"{phrases_file} is not a tsv file"
    assert output_path.suffix == ".tsv", f"{output_path} is not a tsv file"
    transform_resources_group_by_key(phrases_file, output_path)


@app.command()
def extract_keys(resource_path: Path, output: Optional[typer.FileTextWrite] = None):
    """
    Extract all the keys from i18n phrases files under RESOURCE_PATH, structure them into
    tsv files and write to OUTPUT if supplied, or stdout if absent
    """
    assert resource_path.exists(), f"{resource_path} does not exist"
    assert resource_path.is_dir(), f"{resource_path} is not a directory"

    tsv_writer = csv.DictWriter(
        output if output else sys.stdout,
        fieldnames=RESOURCES_TSV_KEY_SET,
        delimiter="\t",
    )
    tsv_writer.writeheader()
    for json_file in resource_path.rglob("*.json"):
        for row in extract_keys_from_file(resource_path, json_file):
            tsv_writer.writerow(row)


@app.command()
def validate_keys(
    scope_key_file: typer.FileText,
    source_code_dir: Path,
    ignore_dynamic_key: bool = True,
    print_unused_phrases: bool = False,
):
    """
    Validate the keys in the source code given by SOURCE_CODE_DIR against the keys in the resource file
    provided in SCOPE_KEY_FILE tsv (transformed by `group_key_locales` script).
    """
    assert source_code_dir.exists(), f"{source_code_dir} does not exist"
    assert source_code_dir.is_dir(), f"{source_code_dir} is not a directory"

    reference_data = load_scope_key_file(scope_key_file)
    count_data = init_count_dict(reference_data)
    unmatched_keys = []

    for line in extract_matched_lines(source_code_dir):
        line_info = LineInfo.from_grep_line(line)

        if (
            line_info.scope not in reference_data
            or line_info.key not in reference_data[line_info.scope]
        ):
            unmatched_keys.append(line_info)
        else:
            count_data[line_info.scope][line_info.key] += 1

    for k in unmatched_keys:
        if k.key_has_str_interpolation():
            if ignore_dynamic_key:
                continue
            error_console.log(
                f"Unmatched key '{k.scope}:{k.key}' which has string interpolation, file='{k.source_file_path}' line_no={k.line_no}"
            )
        else:
            error_console.log(
                f"Unmatched key '{k.scope}:{k.key}', file='{k.source_file_path}' line_no={k.line_no}"
            )

    if print_unused_phrases:
        for scope, key_dict in count_data.items():
            for key, count in key_dict.items():
                if count == 0:
                    error_console.log(
                        f"Key '{scope}:{key}' not in use, locales='{', '.join(reference_data[scope][key])}'"
                    )
