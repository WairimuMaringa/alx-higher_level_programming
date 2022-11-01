-- Script that lists all records with a score >= 10 in second_table of hbtn_0c_0 database in MySQL server
-- Display both score and name respectively. Order is the top first
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
