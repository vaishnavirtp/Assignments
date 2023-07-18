SELECT 
first_name,
last_name,points,
(points +  10) * 100 AS 'discount factor'
FROM customers;

SELECT DISTINCT state 
from customers;

SELECT name,unit_price, (unit_price * 1.1) as 'new unit price'
FROM products;

SELECT * FROM customers
WHERE birth_date > "1990-01-01";

SELECT * FROM orders
WHERE order_date >= "2019-01-01" AND order_date <= "2020-12-31";

SELECT * FROM customers
WHERE points > 2000 OR 
      (birth_date > '1990-01-01' AND state = 'VA');
      
SELECT * FROM customers
WHERE birth_date <= '1990-01-01' AND points <= 1000;

SELECT order_id, quantity, unit_price, unit_price * quantity as total_price
FROM order_items
WHERE order_id = 6 AND unit_price * quantity > 30;

SELECT * FROM customers
WHERE state NOT IN ("VA","GA","FL");

SELECT * FROM products
WHERE quantity_in_stock IN (49,38,72);

SELECT * FROM customers
WHERE points BETWEEN 1000 AND 3000;

SELECT * FROM customers
WHERE birth_date BETWEEN "1990-01-01" AND "2000-01-01";

SELECT * FROM customers
WHERE last_name LIKE 'b____y';
-- % to represent any number of characters
-- _ single character  

SELECT * FROM customers
WHERE address LIKE "%trail%" OR address LIKE "%avenue%";

SELECT * FROM customers
WHERE phone NOT LIKE "%9";

SELECT * FROM customers
WHERE last_name REGEXP "field$|mac|rose";
-- ^ for beginning  
-- $ for ending
-- | for logical
-- [abf] 
--  [a-j]

SELECT * FROM customers
WHERE last_name REGEXP "[g-m]e";

SELECT * FROM customers
WHERE first_name REGEXP "Elka|Ambur";

SELECT * FROM customers
WHERE last_name REGEXP "ey$|on$";

SELECT * FROM customers
WHERE last_name REGEXP "^my|se";

SELECT * FROM customers
WHERE last_name REGEXP "b[ru]";

SELECT * FROM customers
WHERE phone is null;

SELECT * FROM orders
WHERE shipped_date is null;

SELECT * FROM customers
ORDER BY first_name DESC,state DESC;


SELECT *, quantity * unit_price as total
FROM order_items
WHERE order_id = 2
ORDER BY product_id, unit_price * quantity;

SELECT * 
FROM customers
LIMIT 6,3;

SELECT * 
FROM customers
ORDER BY points DESC
LIMIT 3;

-- INNER JOINS 

-- SELECT order_id, o.customer_id, first_name,last_name
-- FROM orders o
-- INNER JOIN customers c ON o.customer_id = c.customer_id;

SELECT order_id, oi.product_id, quantity, p.unit_price, p.name
FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id;


-- JOINING ACROSS DATABASES

SELECT *
FROM order_items oi
JOIN sql_inventory.products p ON oi.product_id = p.product_id;

-- MULTIPLE TABLE JOIN

SELECT o.order_id, o.order_date, c.first_name, c.last_name, os.name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_statuses os ON o.status = os.order_status_id;

-- COMPOUND JOIN

SELECT *
FROM order_items oi
JOIN order_item_notes oin 
ON oi.order_id = oin.order_Id 
AND oi.product_id = oin.product_id;

-- OUTER JOIN
-- LEFT JOIN RETAINS THE VALUES OF LEFT TABLE
-- RIGHT JOIN RETAINS THE VALUES OF RIGHT TABLE

SELECT c.customer_id,c.first_name, o.order_id
FROM orders o 
RIGHT JOIN customers c ON c.customer_id = o.customer_id;

SELECT p.product_id ,p.name, o.quantity
FROM products p
LEFT JOIN order_items o ON o.product_id = p.product_id;

-- MULTIPLE OUTER JOINSELECT c.customer_id,c.first_name, o.order_id
SELECT c.customer_id,c.first_name, o.order_id, s.name as shipper
FROM customers c 
LEFT JOIN orders o  ON c.customer_id = o.customer_id
LEFT JOIN shippers s ON s.shipper_id = o.shipper_id;

SELECT o.order_id, o.order_date,c.first_name, os.name,s.name
FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN shippers s ON s.shipper_id = o.shipper_id
JOIN order_statuses os ON o.status = os.order_status_id;

-- USING CLAUSE

SELECT c.customer_id,c.first_name, o.order_id, s.name as shipper
FROM customers c 
JOIN orders o  USING (customer_id)
LEFT JOIN shippers s USING(shipper_id);


SELECT *
FROM order_items oi
JOIN order_item_notes oin 
USING (order_id,product_id);

SELECT p.date, c.name AS client, p.amount, pm.name
FROM payments p
JOIN payment_methods pm ON pm.payment_method_id = p.payment_method
JOIN clients c USING (client_id)






