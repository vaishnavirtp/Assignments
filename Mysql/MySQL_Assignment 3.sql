-- Difference between blocking and deadlocking.
-- In blocking, one process locks the data and the other process tries to acquire that resource it gets blocks.
-- It needs to wait unless and until the data is not unlocked.alter

-- In deadlocking, the processes are interdependent with each other. 
-- That is one process waits for the other to unlock and the other waits for the first process to 
-- unlock the resource.

--  Delete duplicate data from table only first data remains constant.

DELETE e1 FROM empdata e1, empdata e2
WHERE e1.id > e2.id AND e1.email = e2.email;

SELECT *
FROM empdata;


-- Que-3: Find the Name of Employees.

SELECT id ,COALESCE(name,lastname) as Name
FROM empdata;

-- Que-4: Find the Employees who hired in the Last n months.

SET @n:= 2;
SELECT employee_id,first_name,hire_date,timestampdiff(MONTH,hire_date,CURRENT_DATE()) as Diff
FROM EmployeeInfo 
WHERE timestampdiff(MONTH,hire_date,CURRENT_DATE()) <= @n;

-- Que-5: Find the Employees who hired in the Last n days.

SET @n:= 70;
SELECT employee_id,first_name,hire_date,timestampdiff(DAY,hire_date,CURRENT_DATE()) as Diff
FROM EmployeeInfo 
WHERE timestampdiff(DAY,hire_date,CURRENT_DATE()) <= @n;

-- Que-6: Find the Employees who hired in the Last n years.

SET @n:= 1;
SELECT *,timestampdiff(YEAR,hire_date,CURRENT_DATE()) as Diff
FROM EmployeeInfo 
WHERE timestampdiff(YEAR,hire_date,CURRENT_DATE()) >= @n
ORDER BY hire_date DESC;

-- Que-7: Select all names that start with a given letter.

SELECT first_name 
FROM EmployeeInfo
WHERE first_name REGEXP("^m");

SELECT first_name 
FROM EmployeeInfo
WHERE first_name REGEXP("[ay]");

SELECT first_name 
FROM EmployeeInfo
WHERE first_name REGEXP("^r|y$");
