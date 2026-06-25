-- What was the total sale of products (in $) of each Business Area in the first quarter of 2019?

SELECT
    cd.BUSINESS_NAME
    ,SUM(sl.SALES_VALUE) AS SALES_VALUE
FROM data_store_sales sl
LEFT JOIN data_store_cad cd
ON sl.STORE_CODE = cd.STORE_CODE
WHERE sl.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY
    cd.BUSINESS_NAME


/*
Exploratory analysis:

1.Daily sales by Business Area during Q1 2019.

SELECT
    cd.BUSINESS_NAME
    ,SUM(sl.SALES_VALUE) AS SALES_VALUE
    ,sl.DATE
FROM data_store_sales sl
LEFT JOIN data_store_cad cd
ON sl.STORE_CODE = cd.STORE_CODE
WHERE sl.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY
    cd.BUSINESS_NAME
    ,sl.DATE
;

2.Monthly sales aggregation by Business Area during Q1 2019.

SELECT
    cd.BUSINESS_NAME
    ,SUM(sl.SALES_VALUE) AS SALES_VALUE
    ,CASE WHEN
        MONTH(sl.DATE) = 1 THEN 'Jan'
        WHEN MONTH(sl.DATE) = 2 THEN 'Feb'
        ELSE 'Mar'
    END AS MONTH
FROM data_store_sales sl
LEFT JOIN data_store_cad cd
ON sl.STORE_CODE = cd.STORE_CODE
WHERE sl.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY
    cd.BUSINESS_NAME
    ,MONTH
;
 */