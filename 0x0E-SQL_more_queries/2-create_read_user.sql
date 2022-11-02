-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- This user should only have select privileges in this database and their password set to user_0d_2_pwd
-- if the database, as well as the user already exist, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
