SELECT
    * EXCEPT (date),
    IF(
        REGEXP_CONTAINS(date, "/"),
        PARSE_DATE("%d/%m/%Y", date),
        PARSE_DATE("%d %B %Y", date)
    ) AS date
FROM clinical_trials_raw_v1
