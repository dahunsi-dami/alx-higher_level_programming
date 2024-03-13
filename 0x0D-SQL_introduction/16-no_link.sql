-- lists all records of second_table & rows must have name value
SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL ORDER BY score DESC;
