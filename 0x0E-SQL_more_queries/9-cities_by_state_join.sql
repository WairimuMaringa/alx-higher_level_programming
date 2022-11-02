-- script that lists all cities in the hbtn_0d_usa database
-- each record should display cities.id cities.name states.name and sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
