SELECT 
    prd.name,
    prv.name,
    prd.price
FROM
    products prd
INNER JOIN 
    providers prv
ON prd.id_providers = prv.id
INNER JOIN 
    categories ctg
ON prd.id_categories = ctg.id
WHERE prd.price > 1000 and ctg.name='Super Luxury';
