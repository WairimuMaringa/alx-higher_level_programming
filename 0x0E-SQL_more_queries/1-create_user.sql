-- Script that creates the MySQL server user user_0d_1. this user should have all privileges
-- The user password should be set to user_0d_1_pwd
-- If user exists, script should not fail
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
