SELECT 
    cst.name,
    ord.id
FROM 
    customers cst
INNER JOIN
    orders ord 
ON 
    cst.id = ord.id_customers
WHERE 
    ord.orders_date  BETWEEN '2016-01-01' AND '2016-06-30';