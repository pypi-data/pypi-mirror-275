from pathlib import Path

import duckdb


def transform_resources_group_by_key(resource_file: Path, output_path: Path):
    con = duckdb.connect()

    con.execute(f"""
        CREATE TABLE translations AS
          SELECT * FROM read_csv_auto('{resource_file}', delim='\\t')
    """)

    con.execute(f"""
        COPY (
          SELECT scope, key, listagg(locale order by locale asc, ',') as locales
          FROM translations
          GROUP BY 1, 2
          ORDER BY 1, 2
        ) TO '{output_path}' (HEADER, DELIMITER '\\t')
    """)
