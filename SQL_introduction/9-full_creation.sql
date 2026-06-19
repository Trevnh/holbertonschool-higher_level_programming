-- Creates second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Add John to table
INSERT INTO second_table VALUES(1, "John", 10);
-- Add Alex to table
INSERT INTO second_table VALUES(2, "Alex", 3);
-- Add Bob to table
INSERT INTO second_table VALUES(3, "Bob", 14);
-- Add George to table
INSERT INTO second_table VALUES(4, "George", 8)
