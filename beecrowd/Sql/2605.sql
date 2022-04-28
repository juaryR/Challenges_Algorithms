 
--   2605 - Representantes Executivos 
SELECT 
    products.name,
    providers.name
FROM providers
INNER JOIN products
    ON providers.id = id_providers
INNER JOIN categories
    ON categories.id = products.id_categories
where categories.id ='6';