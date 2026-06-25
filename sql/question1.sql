-- What are the 10 most expensive products in the company?
# DESCRIBE  data_product
SELECT
    PRODUCT_COD # prod code
    ,PRODUCT_NAME # prod name
    ,PRODUCT_VAL # prod value
FROM data_product
WHERE PRODUCT_VAL IS NOT NULL
ORDER BY PRODUCT_VAL DESC # order by most expensive
LIMIT 10; # question asks for top 10
