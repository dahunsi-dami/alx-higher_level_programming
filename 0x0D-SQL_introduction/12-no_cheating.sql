-- update Bob's score to 10 in second_table without using Bob's id value, only name
UPDATE second_table SET `score` = 10 WHERE name = 'Bob';
