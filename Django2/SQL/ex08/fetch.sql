SELECT 
    p.name AS character_name, 
    p.homeworld, 
    pl.climate
FROM
    ex08_people p
JOIN
    ex08_planets pl ON p.homeworld = pl.name
WHERE
    pl.climate LIKE  '%windy%'
ORDER BY
    p.name ASC;
