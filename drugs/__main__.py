"""Entrypoint for the test, each sub-command represent a part of the subject."""

import rich_click as click

from drugs.ingest import ingest_drugs


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


if __name__ == "__main__":
    do_drugs()
