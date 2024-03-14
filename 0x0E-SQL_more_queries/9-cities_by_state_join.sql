-- lists cities in hbtn_0d_usa database
-- display cities.id, cities.name, states.name
-- sort results in ascending order by cities.id
-- only use SELECT statement
-- db name will be passed as argument of mysql command

SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY id;
