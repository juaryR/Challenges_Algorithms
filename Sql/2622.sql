SELECT 
    c.name 
FROM
    customers c 
LEFT JOIN 
    legal_person L
ON 
    c.id = l.id_customers
WHERE 
    cnpj IS NOT NULL;