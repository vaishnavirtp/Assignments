USE sql_hr;

-- SELF JOIN 
SELECT e.employee_id, e.first_name, m.first_name AS manager
FROM employees e
JOIN employees m ON e.reports_to = m.employee_id;

USE sql_invoicing;

SELECT c.name, pm.name as payment_method, p.date, p.amount
FROM payments p
JOIN clients c ON p.client_id = c.client_id
JOIN payment_methods pm ON pm.payment_method_id = p.payment_method;


-- SELF OUTER JOIN

SELECT e.employee_id, e.first_name, m.first_name AS manager
FROM employees e
LEFT JOIN employees m ON e.reports_to = m.employee_id;



