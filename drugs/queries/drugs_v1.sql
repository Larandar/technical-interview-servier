WITH drug_pubmed AS (
    SELECT atcode,
        drug,
        ARRAY_AGG(STRUCT(journal, id, date)) AS pubmed
    FROM drugs_raw_v1
        CROSS JOIN pubmed_v1
    WHERE REGEXP_CONTAINS(LOWER(title), LOWER(drug))
    GROUP BY atcode,
        drug
),
drug_clinical_trials AS (
    SELECT atcode,
        drug,
        ARRAY_AGG(STRUCT(journal, id, date)) AS clinical_trials
    FROM drugs_raw_v1
        CROSS JOIN clinical_trials_v1
    WHERE REGEXP_CONTAINS(LOWER(scientific_title), LOWER(drug))
    GROUP BY atcode,
        drug
)

SELECT drugs.atcode,
    drugs.drug,
    clinical_trials,
    pubmed
FROM drugs_raw_v1 AS drugs
    FULL JOIN drug_pubmed ON drugs.atcode = drug_pubmed.atcode
    FULL JOIN drug_clinical_trials ON drugs.atcode = drug_clinical_trials.atcode