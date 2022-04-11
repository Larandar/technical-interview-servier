"""Injest files into bigquery."""
import json
import tempfile
from pathlib import Path

from drugs.operators import bq_load_operator, bq_mk_dataset_operator

TMP_SCHEMA: Path = None


def schema_file(schema: dict) -> Path:
    """Create a schema file from a dictionary."""
    global TMP_SCHEMA
    if TMP_SCHEMA is None or not TMP_SCHEMA.exists():
        TMP_SCHEMA = Path(tempfile.mkstemp(suffix="_schema.json")[1])

    with TMP_SCHEMA.open("w") as f:
        json.dump(schema, f)

    return TMP_SCHEMA


def ingest_drugs(dataset: str):
    """Ingest files into bigquery as raw as possible."""
    bq_mk_dataset_operator(dataset)

    bq_load_operator(
        f"{dataset}.drugs_raw_v1",
        Path("inputs/drugs.csv"),
        schema_file(
            [
                dict(name="atcode", type="STRING", mode="REQUIRED"),
                dict(name="drug", type="STRING", mode="REQUIRED"),
            ]
        ),
    )
    bq_load_operator(
        f"{dataset}.clinical_trials_raw_v1",
        Path("inputs/clinical_trials.csv"),
        schema_file(
            [
                dict(name="id", type="STRING", mode="REQUIRED"),
                dict(name="scientific_title", type="STRING", mode="REQUIRED"),
                dict(name="date", type="STRING", mode="REQUIRED"),
                dict(name="journal", type="STRING", mode="REQUIRED"),
            ]
        ),
    )
    bq_load_operator(
        f"{dataset}.pubmed_raw_v1",
        Path("inputs/pubmed.csv"),
        schema_file(
            [
                dict(name="id", type="INTEGER", mode="REQUIRED"),
                dict(name="title", type="STRING", mode="REQUIRED"),
                dict(name="date", type="STRING", mode="REQUIRED"),
                dict(name="journal", type="STRING", mode="REQUIRED"),
            ]
        ),
    )

    TMP_SCHEMA.unlink()
