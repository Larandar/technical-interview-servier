"""Entrypoint for the test, each sub-command represent a part of the subject."""
from pathlib import Path

import rich_click as click

import drugs.ingest


@click.group()
def do_drugs():
    """Drugs is a collection of tools for data analysis."""
    pass


@do_drugs.command()
def ingest():
    """Ingest files into bigquery."""
    drugs.ingest.bq_mk_dataset_operator("drugs_raw")
    drugs.ingest.bq_load_operator(
        "drugs_raw.drugs_v1", Path("inputs/drugs.csv"), "atcode:STRING,drug:STRING"
    )
    drugs.ingest.bq_load_operator(
        "drugs_raw.clinical_trials_v1",
        Path("inputs/clinical_trials.csv"),
        "id:STRING,scientific_title:STRING,date:STRING,journal:STRING",
    )
    drugs.ingest.bq_load_operator(
        "drugs_raw.pubmed_v1",
        Path("inputs/pubmed.csv"),
        "id:INTEGER,title:STRING,date:STRING,journal:STRING",
    )


if __name__ == "__main__":
    do_drugs()
