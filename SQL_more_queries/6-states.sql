-- Creates hbtn_0d_usa database to MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates states table to hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
