-- script listing all states of california that are present in hbtn_0d_usa database
-- states table contains only one record where name = california but id can be different
-- results should be sorted in ascending order
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states WHERE name = "California"
);
