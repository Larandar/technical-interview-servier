"""Entrypoint for the test, each sub-command represent a part of the subject."""

from pathlib import Path

import rich_click as click

from drugs.analysis import analyse_drugs
from drugs.ingest import ingest_drugs
from drugs.transform import transform_drugs


@click.group()
@click.option("--dataset", default="servier_drugs")
@click.pass_context
def do_drugs(ctx, dataset: str):
    """Drugs is a collection of tools for data analysis."""
    ctx.obj = {"dataset": dataset}


@do_drugs.command()
@click.pass_context
def ingest(ctx):
    """Ingest files into bigquery."""
    ingest_drugs(ctx.obj["dataset"])


@do_drugs.command()
@click.pass_context
def transform(ctx):
    """Process raw drug data for data warehousing."""
    transform_drugs(ctx.obj["dataset"])


@do_drugs.command()
def analyse():
    """Analyse the data."""
    result = analyse_drugs(Path("drugs_v1.json"))
    click.secho(f"Journal with most cited drugs: {result}", fg="green")


if __name__ == "__main__":
    do_drugs()
