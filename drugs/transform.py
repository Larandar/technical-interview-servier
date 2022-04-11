"""Process raw drug data for data warehousing."""

from pathlib import Path

from drugs.operators import (
    bq_extract_operator,
    bq_query_operator,
    gs_ensure_bucket_operator,
)


def transform_drugs(dataset: str):
    """Ingest files into bigquery as raw as possible."""
    bq_query_operator(dataset, "pubmed_v1", Path("drugs/queries/pubmed_v1.sql"))
    bq_query_operator(
        dataset,
        "clinical_trials_v1",
        Path("drugs/queries/clinical_trials_v1.sql"),
    )
    bq_query_operator(dataset, "drugs_v1", Path("drugs/queries/drugs_v1.sql"))

    gs_bucket = dataset.replace("_", "-")
    gs_ensure_bucket_operator(gs_bucket)
    bq_extract_operator(
        dataset,
        "drugs_v1",
        f"gs://{gs_bucket}/extracts/drugs_v1.json",
    )
