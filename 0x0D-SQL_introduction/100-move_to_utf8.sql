-- Script that converts hbtn_0c_0 database to UTF8 in a MySQL server
-- Database hbtn_0c_0, first_table and the field name in first_table should all be converted to UTF-8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
