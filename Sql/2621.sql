SELECT 
    prd.name
FROM 
    products prd
INNER JOIN 
    providers pvr
ON 
    prd.id_providers = pvr.id
WHERE
    pvr.name LIKE 'P%' AND
    prd.amount BETWEEN 10 AND 20 ;