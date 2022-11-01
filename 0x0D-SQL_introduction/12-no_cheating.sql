-- Script that updates the score of Bob to 10 in second_table
-- Not allowed to use Bobs id value, only the name field
UPDATE second_table
SET score = 10
WHERE name = "Bob";
