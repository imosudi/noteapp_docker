/*
GRANT ALL PRIVILEGES ON noteappdb.* TO noteappdb@ALL IDENTIFIED BY 'password';
*/
FLUSH PRIVILEGES;
/*CREATE USER 'jack'@'localhost' IDENTIFIED BY 'test123';*/
CREATE USER 'noteappdb'@'localhost' IDENTIFIED BY 'password';

/*CREATE USER 'noteappdb'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

ALTER USER 'noteappdb'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';*/

GRANT ALL PRIVILEGES ON noteappdb.* TO 'noteappdb'@'localhost' ;
CREATE TABLE users ( 
	id INT(50) NOT NULL AUTO_INCREMENT , 
	email VARCHAR(150) NULL DEFAULT NULL , 
	name VARCHAR(150) NULL DEFAULT NULL , 
	username VARCHAR(150) NULL DEFAULT NULL , 
	password VARCHAR(150) NULL DEFAULT NULL , 
	INDEX (id)) ENGINE = InnoDB;

CREATE TABLE notes ( 
	id INT(50) NOT NULL AUTO_INCREMENT , 
	title VARCHAR(100) NULL DEFAULT NULL , 
	body VARCHAR(450) NULL DEFAULT NULL , 
	username VARCHAR(150) NULL DEFAULT NULL , 
	INDEX (id)) ENGINE = InnoDB;

FLUSH PRIVILEGES;
