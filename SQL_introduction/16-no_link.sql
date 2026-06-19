-- Lists all records of second_table except empty name, show score and name, listed by score in descending order
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY `score` DESC;
