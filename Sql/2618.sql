SELECT 
    prd.name,
    pvd.name,
    ctg.name
FROM products prd
INNER JOIN providers pvd
ON prd.id_providers = pvd.id
INNER JOIN categories ctg
ON prd.id_categories = ctg.id
WHERE pvd.name = 'Sansul SA' and ctg.name = 'Imported';