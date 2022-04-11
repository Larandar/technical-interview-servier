SELECT
    * EXCEPT (date),
    IF(
        REGEXP_CONTAINS(date, "/"),
        PARSE_DATE("%d/%m/%Y", date),
        PARSE_DATE("%Y-%m-%d", date)
    ) AS date
FROM pubmed_raw_v1
