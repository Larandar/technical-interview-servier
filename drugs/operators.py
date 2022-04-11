"""Fake 'Operators' to replace with Airflow in production."""

import subprocess
from pathlib import Path


def bq_mk_dataset_operator(dataset_name: str):
    """Create a dataset in bigquery using the `bq` binary.

    Notes:
    - This treatment would be delegated to Terraform (or any other IaC tool).
    - This operator use the credentials project by design.
    """
    subprocess.run(["bq", "mk", "-d", dataset_name])


def bq_load_operator(table_ref: str, file: Path, schema: str):
    """Load a file into bigquery using the `bq` binary.

    Notes:
    - This treatment would be delegated to a PodOperator that would
      use the `google/cloud-sdk` image with the configured credentials.
    - This operator use the credentials project by design.
    """
    subprocess.run(
        [
            "bq",
            "load",
            "--source_format=CSV",
            "--skip_leading_rows=1",
            "--replace",
            table_ref,
            file,
            schema,
        ]
    )


def bq_query_operator(dataset: str, destination_table: str, query_file: Path):
    """Query a bigquery table using the `bq` binary.

    Notes:
    - This treatment would be delegated to a PodOperator that would
      use the `google/cloud-sdk` image with the configured credentials.
    - This operator use the credentials project by design.
    """
    with query_file.open("r") as query:
        subprocess.run(
            [
                "bq",
                "query",
                "--use_legacy_sql=false",
                "--replace",
                f"--dataset_id={dataset}",
                f"--destination_table={destination_table}",
                "--append_table",
                query.read(),
            ],
        )
