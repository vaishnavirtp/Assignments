CREATE DATABASE Assign2DB;

 INSERT INTO departments VALUES ( 30,'Purchasing',  1700);
 INSERT INTO departments VALUES ( 40, 'Human Resources',  2400);
 INSERT INTO departments VALUES ( 50, 'Shipping',  1500);
 INSERT INTO departments VALUES ( 60 , 'IT',  1400);
 INSERT INTO departments VALUES ( 70, 'Public Relations',  2700);
 INSERT INTO departments VALUES ( 80 , 'Sales',  2500 );
 INSERT INTO departments VALUES ( 90 , 'Executive',  1700);
 INSERT INTO departments VALUES ( 100 , 'Finance',  1700);
 INSERT INTO departments VALUES ( 110 , 'Accounting',  1700);
 INSERT INTO departments VALUES ( 120 , 'Treasury' ,  1700);
 INSERT INTO departments VALUES ( 130 , 'Corporate Tax' ,  1700 );
 INSERT INTO departments VALUES ( 140, 'Control And Credit' ,  1700);
 INSERT INTO departments VALUES ( 150 , 'Shareholder Services', 1700);
 INSERT INTO departments VALUES ( 160 , 'Benefits', 1700);
 INSERT INTO departments VALUES ( 170 , 'Payroll' , 1700);

INSERT INTO employees VALUES (102 , 'Lex' , 'De Haan' , 'LDEHAAN' , '515.123.4569' , '1993-09-12' , 'AD_VP' , 17000 , NULL , 100 , 30);
INSERT INTO employees VALUES (103 , 'Alexander' , 'Hunold' , 'AHUNOLD' , '590.423.4567' , '1990-09-30', 'IT_PROG' , 9000 , NULL , 102 , 60);
INSERT INTO employees VALUES (104 , 'Bruce' , 'Ernst' , 'BERNST' , '590.423.4568' , '1991-05-21',  'IT_PROG' , 6000 , NULL , 103 , 60);
INSERT INTO employees VALUES (105 , 'David' , 'Austin' , 'DAUSTIN' , '590.423.4569' , '1997-06-25',  'IT_PROG' , 4800 , NULL , 103 , 60);
INSERT INTO employees VALUES (106 , 'Valli' , 'Pataballa' , 'VPATABAL' , '590.423.4560' , '1998-02-05',  'IT_PROG' , 4800 , NULL , 103 , 40);
INSERT INTO employees VALUES (107 , 'Diana' , 'Lorentz' , 'DLORENTZ' , '590.423.5567' , '1999-02-09',  'IT_PROG' , 4200 , NULL , 103 , 40);
INSERT INTO employees VALUES (108 , 'Nancy' , 'Greenberg' , 'NGREENBE' , '515.124.4569' , '1994-08-17',  'FI_MGR' , 12000 , NULL , 101 , 100);
INSERT INTO employees VALUES (109 , 'Daniel' , 'Faviet' , 'DFAVIET' , '515.124.4169' , '1994-08-12',  'FI_ACCOUNT' , 9000 , NULL , 108 , 170);
INSERT INTO employees VALUES (110 , 'John' , 'Chen' , 'JCHEN' , '515.124.4269' , '1997-04-09',  'FI_ACCOUNT' , 8200 , NULL , 108 , 170);
INSERT INTO employees VALUES (111 , 'Ismael' , 'Sciarra' , 'ISCIARRA' , '515.124.4369' , '1997-02-01',  'FI_ACCOUNT' , 7700 , NULL , 108 , 160);
INSERT INTO employees VALUES (112 , 'Jose Manuel' , 'Urman' , 'JMURMAN' , '515.124.4469' , '1998-06-03', 'FI_ACCOUNT' , 7800 , NULL , 108 , 150);
INSERT INTO employees VALUES (113 , 'Luis' , 'Popp' , 'LPOPP' , '515.124.4567' , '1999-12-07',  'FI_ACCOUNT' , 6900 , NULL , 108 , 140);
INSERT INTO employees VALUES (114 , 'Den' , 'Raphaely' , 'DRAPHEAL' , '515.127.4561' , '1994-11-08',  'PU_MAN' , 11000 , NULL , 100 , 30);
INSERT INTO employees VALUES (115 , 'Alexander' , 'Khoo' , 'AKHOO' , '515.127.4562' , '1995-05-12',  'PU_CLERK' , 3100 , NULL , 114 , 80);
INSERT INTO employees VALUES (116 , 'Shelli' , 'Baida' , 'SBAIDA' , '515.127.4563' ,'1997-12-13', 'PU_CLERK' , 2900 , NULL , 114 , 70);
INSERT INTO employees VALUES (117 , 'Sigal' , 'Tobias' , 'STOBIAS' , '515.127.4564' , '1997-09-10', 'PU_CLERK' , 2800 , NULL , 114 , 30);
INSERT INTO employees VALUES (118 , 'Guy' , 'Himuro' , 'GHIMURO' , '515.127.4565' , '1998-01-02',  'PU_CLERK' , 2600 , NULL , 114 , 60);
INSERT INTO employees VALUES (119 , 'Karen' , 'Colmenares' , 'KCOLMENA' , '515.127.4566' , '1999-04-08',  'PU_CLERK' , 2500 , NULL , 114 , 130);
INSERT INTO employees VALUES (120 , 'Matthew' , 'Weiss' , 'MWEISS' , '650.123.1234' ,'1996-07-18',  'ST_MAN' , 8000 , NULL , 100 , 50);
INSERT INTO employees VALUES (121 , 'Adam' , 'Fripp' , 'AFRIPP' , '650.123.2234' , '1997-08-09',  'ST_MAN' , 8200 , NULL , 100 , 50);
INSERT INTO employees VALUES (122 , 'Payam' , 'Kaufling' , 'PKAUFLIN' , '650.123.3234' ,'1995-05-01',  'ST_MAN' , 7900 , NULL , 100 , 40);
INSERT INTO employees VALUES (123 , 'Shanta' , 'Vollman' , 'SVOLLMAN' , '650.123.4234' , '1997-10-12',  'ST_MAN' , 6500 , NULL , 100 , 50);
INSERT INTO employees VALUES (124, 'Kevin' , 'Mourgos' , 'KMOURGOS' , '650.123.5234' , '1999-11-12',  'ST_MAN' , 5800 , NULL , 100 , 80);
INSERT INTO employees VALUES (125, 'Julia' , 'Nayer' , 'JNAYER' , '650.124.1214' , '1997-07-02',  'ST_CLERK' , 3200 , NULL , 120 , 50);
INSERT INTO employees VALUES (126, 'Irene' , 'Mikkilineni' , 'IMIKKILI' , '650.124.1224' , '1998-11-12', 'ST_CLERK' , 2700 , NULL , 120 , 50);
INSERT INTO employees VALUES (127, 'James' , 'Landry' , 'JLANDRY' , '650.124.1334' , '1999-01-02' , 'ST_CLERK' , 2400 , NULL , 120 , 90);
INSERT INTO employees VALUES (128, 'Steven' , 'Markle' , 'SMARKLE' , '650.124.1434' , '2000-03-04' , 'ST_CLERK' , 2200 , NULL , 120 , 50);
INSERT INTO employees VALUES (129, 'Laura' , 'Bissot' , 'LBISSOT' , '650.124.5234' ,'1997-09-10' , 'ST_CLERK' , 3300 , NULL , 121 , 50);
INSERT INTO employees VALUES (130, 'Mozhe' , 'Atkinson' , 'MATKINSO' , '650.124.6234' , '1997-10-12' , 'ST_CLERK' , 2800 , NULL , 121 , 110);

-- 1. Select employees first name, last name, job_id and salary whose first name starts with alphabet S 

SELECT first_name, last_name, job_id, salary
FROM employees 
WHERE first_name REGEXP("^s");

-- 2. Write a query to select employee with the highest salary

SELECT *
FROM employees 
ORDER BY salary DESC
LIMIT 2 OFFSET 1;

-- 4. Fetch employees with 2nd or 3rd highest salary

set @input := 3;
SELECT *
FROM employees e
WHERE @input = (SELECT COUNT(salary) FROM employees p WHERE e.salary <= p.salary);

-- 5. Write a query to select employees and their corresponding managers and their salaries

SELECT e.first_name, e.last_name, e.manager_id, p.first_name
FROM employees e
JOIN employees p ON e.manager_id = p.employee_id;

-- 6. Write a query to show count of employees under each manager in descending order

 select 
 sup.employee_id ,
     concat(sup.first_name,' ', sup.last_name) AS manager_name,
     COUNT(sub.employee_id) AS number_of_reportees
 from employees sub 
 join employees sup 
 on sub.manager_id = sup.employee_id
 group by sup.employee_id, sup.first_name, sup.last_name
 order by 3 desc;
 
 -- 7. Find the count of employees in each department
 
 SELECT d.department_id, d.department_name, 
 COUNT(e.department_id) AS employees
 FROM departments d
 JOIN employees e ON e.department_id = d.department_id
 GROUP BY e.department_id;
 
 -- 8. Get the count of employees hired year wise
SELECT YEAR(hire_date) hire_date,COUNT(*) employee_count 
FROM employees
GROUP BY YEAR(hire_date);

-- 9. Find the salary range of employees
SELECT salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees) or salary = (SELECT MIN(salary) FROM employees);


SELECT MIN(salary) AS min_salary,
MAX(salary) AS max_salary,
AVG(salary) AS avg_salary
FROM employees;

-- 10. Write a query to divide people into three groups based on their salaries.

SELECT CONCAT(first_name, ' ', last_name) employee,
salary,
CASE
WHEN salary BETWEEN 2000 AND 10000 THEN "low"
WHEN salary BETWEEN 10000 AND 18000 THEN "mid"
ELSE "high"
END AS salary_group
FROM employees
ORDER BY 2 DESC;


-- 11. Select the employees whose first_name contains “an”

SELECT *
FROM employees
WHERE first_name LIKE "%an%";


-- 12. Select employee first name and the corresponding phone number in the format (_ _ _)-(_ _ _)-(_ _ _ _
SELECT first_name AS name,REPLACE(phone_number,'.','-') phone_number
FROM employees;

-- 13. Find the employees who joined in August, 1994.

SELECT first_name, hire_date
FROM employees
WHERE hire_date >= "1994-08-01" AND hire_date <= "1994-08-31";


SELECT first_name, hire_date
FROM employees
WHERE YEAR(hire_date) = "1994" AND MONTH(hire_date) = "08";


-- 14. Write an SQL query to display employees who earn more than the average salary in that company

SELECT * 
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 15. Find the maximum salary from each department.

SELECT d.department_name, d.department_id, MAX(salary) AS max_salary
FROM departments d
JOIN employees e USING(department_id)
GROUP BY e.department_id
ORDER BY 2;


-- 16. Write a SQL query to display the 5 least earning employees

SELECT *
FROM employees
ORDER BY salary
LIMIT 5;

-- 

-- 17. Find the employees hired in the 80s

SELECT first_name,YEAR(hire_date) AS hire_date
FROM employees 
WHERE YEAR(hire_date) < "1990" AND YEAR(hire_date) > "1980";

-- 18. Display the employees first name and the name in reverse order
SELECT first_name, REVERSE(first_name) AS reverse_first_name ,last_name ,REVERSE(last_name) AS reverse_last_name
FROM employees;

-- 19. Find the employees who joined the company after 15th of the month

SELECT first_name,hire_date 
FROM employees 
WHERE DAY(hire_date) > "15";

-- 20. Display the managers and the reporting employees who work in different departments

SELECT 
CONCAT(m.first_name, ' ', m.last_name) manager, 
CONCAT(e.first_name,' ',e.last_name) employee, 
m.department_id AS manager_dep,
e.department_id AS emp_dep
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE e.department_id != m.department_id;


SELECT 
CONCAT(m.first_name, ' ', m.last_name) manager, 
COUNT(e.employee_id) employee_count
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
GROUP BY e.manager_id;