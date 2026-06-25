-- What are the 10 most expensive products in the company?
SELECT
    PRODUCT_COD
    ,PRODUCT_NAME
    ,PRODUCT_VAL
FROM data_product
WHERE PRODUCT_VAL IS NOT NULL
ORDER BY PRODUCT_VAL DESC
LIMIT 10;
