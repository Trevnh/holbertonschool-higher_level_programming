-- Creates hbtn_0d_2 database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates user_0d_2 with password user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant user_0d_2 SELECT privilege in hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
