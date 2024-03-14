-- 8-cities_of_california_subquery.sql
-- Lists all the cities of California without using JOIN keyword
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
