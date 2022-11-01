-- Script that lists all records of second_table of database hbtn_0c_0 in MySQL server
-- Rows without name value should not be listed
-- score and name to be listed respectively
-- descending order to be used
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
