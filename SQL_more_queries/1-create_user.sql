-- Creates user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost';
