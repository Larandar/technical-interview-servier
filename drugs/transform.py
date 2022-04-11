"""Process raw drug data for data warehousing."""

from pathlib import Path

from drugs.operators import bq_query_operator


def transform_drugs(dataset: str):
    """Ingest files into bigquery as raw as possible."""
    bq_query_operator(dataset, "pubmed_v1", Path("drugs/queries/pubmed_v1.sql"))
    bq_query_operator(
        dataset, "clinical_trials_v1", Path("drugs/queries/clinical_trials_v1.sql")
    )
