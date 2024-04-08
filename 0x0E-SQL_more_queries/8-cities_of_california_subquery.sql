-- lists cities of California in hbtn_0d_usa database
-- sort results in ascending order by cities.id
-- do NOT use the JOIN keyword
-- db name will be passed as argument of mysql command

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
