"""Injest files into bigquery."""
from pathlib import Path

from drugs.operators import bq_load_operator, bq_mk_dataset_operator


def ingest_drugs(dataset: str):
    """Ingest files into bigquery as raw as possible."""
    bq_mk_dataset_operator(dataset)
    bq_load_operator(
        f"{dataset}.drugs_raw_v1",
        Path("inputs/drugs.csv"),
        "atcode:STRING,drug:STRING",
    )
    bq_load_operator(
        f"{dataset}.clinical_trials_raw_v1",
        Path("inputs/clinical_trials.csv"),
        "id:STRING,scientific_title:STRING,date:STRING,journal:STRING",
    )
    bq_load_operator(
        f"{dataset}.pubmed_raw_v1",
        Path("inputs/pubmed.csv"),
        "id:INTEGER,title:STRING,date:STRING,journal:STRING",
    )
