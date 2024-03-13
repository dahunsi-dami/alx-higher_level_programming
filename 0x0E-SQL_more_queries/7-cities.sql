-- creates database `hbtn_0d_usa` and table `cities` w/ description:
-- id INT unique, auto generated, can't be null & is a primary key
-- state_id INT, can't be null, must be a foreign key referencing id of `states` table
-- name VARCHAR, 256 can't be null
-- if database based already exists, script shouldn't fail
-- if table already exists, script shouldn't fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL
	);
