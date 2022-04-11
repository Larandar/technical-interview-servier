SELECT
    date,
    SUM(price) AS ventes
FROM (
    SELECT
        date,
        prod_price * prod_qty as price
    FROM transaction
) AS transaction
WHERE
    date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY date
