-- 1. Write a mysql statement to find the concatenated first_name, last_name where the age of the employee is greater than 30.

SELECT CONCAT(first_name , " ",last_name) 
FROM employee
WHERE age > 30;

-- 2. Write a mysql statement to get user, current date and mysql version.

SELECT user(), current_date(), version();

-- 3. Write a mysql statement to get item id, item, price of the most expensive item.

SELECT item_id, item, price 
FROM items
WHERE price = (SELECT MAX(price) from items);

-- 4. Write a mysql statement to create a new user and set a password and privileges for an existing database.

CREATE USER 'vaishmysql'@'localhost' IDENTIFIED BY 'Vaish*sql123';
GRANT SELECT, INSERT ON movies.* TO 'vaishmysql'@'localhost';
SHOW GRANTS FOR 'vaishmysql'@'localhost';

-- 5. Write a mysql statement to select data of only CS and IT departments.
SELECT * 
FROM students
WHERE department = "CS" OR department = "IT";

-- 6. Write a mysql statement to select data of all departments in descending order by age.
SELECT departments
FROM students
ORDER BY age DESC;

-- 7. Write a mysql statement to determine the age of each of the students.

SELECT first_name,last_name, birth, TIMESTAMPDIFF(YEAR,birth,current_date()) as age
FROM EmployeeInfo;

-- 8. Write a mysql statement to retrieve name beginning with 'm'.

SELECT first_name 
FROM EmployeeInfo
WHERE first_name LIKE "m%";

-- 9. Write a mysql statement to find the name, birth, department name, department block from the given tables.

SELECT name, birth, dept_name, dept_block
FROM students s
JOIN departments d ON d.dept_id = s.dept_id; 

-- 10. Write a mysql statement to get name of students containing exactly four characters.

SELECT first_name
FROM EmployeeInfo
WHERE first_name LIKE "____";

CREATE TABLE IF NOT EXISTS `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

INSERT INTO `students` (`id`, `first_name`, `last_name`, `email`) VALUES
(1, 'John', 'Smith', 'john@example.com'),
(2, 'Soyam', 'Mithal', 's.mithal@example.com'),
(3, 'Rohan', 'Soy', 'rohan.soy@example.com'),
(4, 'Rita', 'Smith', 'rita@example.com'),
(5, 'John', 'Smith', 'john@example.com'),
(6, 'Sayam', 'Mitra', 'sayam.mitra@example.com'),
(7, 'Shyam', 'Mishra', 'shyam@example.com'),
(8, 'Soyam', 'Mithal', 's.mithal@example.com'),
(9, 'Rohan', 'Soy', 'rohan.soy@example.com'),
(10, 'Mita', 'Dahl', 'mita@example.com');

DELETE s1 from students s1, students s2
WHERE s1.email = s2.email and s1.id > s2.id;

SELECT * 
FROM students;

-- 12. Display the alternate rows from MySQL table.

SELECT * 
FROM students 
GROUP BY id having mod(id,2)=0;

-- 13. Delete alternate rows from MySQL table.

DELETE
FROM students 
WHERE mod(id,2) = 0;

SELECT * 
FROM students;

-- 14. MySQL update multiple rows in one query.

CREATE TABLE IF NOT EXISTS `empdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

INSERT INTO `empdata` (`id`, `name`, `email`, `phone`) VALUES
(1, 'Anjali', 'anjali@example.com', 878433948),
(2, 'Priska', 'priska@example.com', 493905490),
(3, 'Abhi', 'abhi@example.com', 403022139),
(4, 'Joya', 'joya@example.com', 342345329),
(5, 'Ammy', 'ammy@example.com', 239848342),
(6, 'Lussi', 'lussi@example.com', 490290331);


UPDATE empdata
SET phone = CASE
WHEN id = 1 THEN "387391739"
WHEN id = 2 THEN "782739739"
ELSE phone
END;


SELECT *
FROM empdata;

-- 15. MySQL get nth highest paid and nth lowest paid salary.

CREATE TABLE IF NOT EXISTS `empsalary`
(
`id` INT(11) NOT NULL AUTO_INCREMENT,
`salary` INT(50) NOT NULL,
`fullname` VARCHAR(50) NOT NULL,
PRIMARY KEY(`id`)
) ENGINE=MyISAM AUTO_INCREMENT 7 DEFAULT CHARSET = latin1;



INSERT INTO `empsalary` (`id`,`fullname`,`salary`) VALUES
(1,"Vaishnavi Ranbhare",20000),
(2, 'Joney', 20000),
(3, 'Mariya', 40000),
(4, 'Zoya Aktar', 35000),
(5, 'Smith Rajaram', 25000),
(6, 'Rosy', 75000);

SELECT * 
FROM empsalary
WHERE salary = (SELECT  MAX(salary) FROM empsalary) OR salary = (SELECT  MIN(salary) FROM empsalary);


-- 16. Display the nth row from MySQL table.
SELECT *
FROM empsalary
ORDER BY id
LIMIT 2 OFFSET 4;

-- 17. Write a MySQL statements for rollback commit and save points.

CREATE TABLE item_order(item_id INT, name CHAR(50), INDEX (item_id));
START TRANSACTION;

INSERT INTO item_order VALUES(101,"Bread");
COMMIT;

SET autocommit=0;

INSERT INTO item_order VALUES (102, 'Jam');
INSERT INTO item_order VALUES (103, 'Oranges');

SAVEPOINT C;

DELETE from item_order 
WHERE name = "Oranges";

SELECT *
FROM item_order;

ROLLBACK TO C;

SELECT *
FROM item_order;

-- 18. Display details of first 5 highly paid employees using MySQL.

SELECT *
FROM empsalary
ORDER BY salary DESC
LIMIT 3;


