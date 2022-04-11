# Servier - Test Adrien DUDOUIT

## Data Pipeline and Ad-Hoc analysis

The project is structured this way:

- `drugs/ingest.py`: ingestion of raw data (I.3)
- `drugs/transform.py`: data cleaning and warehousing (I.3)
- `drugs/analysis.py`: ad-hoc analysis (I.4)

### Options 1: ELT witch BigQuery

| Pros                                       | Cons                       |
|--------------------------------------------|----------------------------|
| Easy to implement                          | Harder for data-wrangling  |
| Easy to run in production                  |                            |
| Lower barrier of entry for non-developper  |                            |

## Options 2: ETL with Dataflow

| Pros                      | Cons                                                   |
|---------------------------|--------------------------------------------------------|
| Easier for data-wrangling | Harder to implement                                    |
|                           | Barrier of entry for developper                        |
|                           | Extreme care must be given to monitoring at all levels |

### Scaling considerations

All processing being made by bigquery (or dataflow) means scaling is only limited by costs and
quotas. In my opinion no ad-hoc (pure python or pandas) should ever be used in production as it
does not scale well and is not worth the ease of implementation for a data pipeline.

For considerations when scaling:

- SQL queries can be optimized.
- Maybe an hybrid of the two options (tagging in dataflow + processing in bq) can be more efficient
  but it would need to be benchmarked at scale.

## SQL analysis

The SQL queries are written in the following files:

- `transactions/daily_sales.sql`: daily sales (II.2)
- `transactions/by_client.sql`: sales by types by client (II.3)
