SELECT 
    prd.name,
    ctg.name 
FROM 
    products prd
INNER JOIN 
    categories ctg
ON 
    ctg.id = prd.id_categories
WHERE
    prd.amount >= 100 and
    ctg.id IN (1,2,3,6,9)
ORDER BY
	ctg.id ASC;