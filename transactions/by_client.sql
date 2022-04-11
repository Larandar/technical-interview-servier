SELECT
    client_id
    SUM(IF(is_meuble, prod_qty, 0)) AS ventes_meuble,
    SUM(IF(is_deco, prod_qty, 0)) AS ventes_deco,
FROM (
    SELECT
        client_id,
        date,
        prod_qty,
        product_type = "MEUBLE" AS is_meuble,
        product_type = "DECORATION" AS is_deco,
    FROM transaction
    JOIN product_nomenclature ON transaction.prod_id = product_nomenclature.product_id
) AS transaction
WHERE
    date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY client_id
