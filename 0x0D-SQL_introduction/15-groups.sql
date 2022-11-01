-- Script that lists number of records with the same score in second_table in hbtn_0c_0 database in MySQL server
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
