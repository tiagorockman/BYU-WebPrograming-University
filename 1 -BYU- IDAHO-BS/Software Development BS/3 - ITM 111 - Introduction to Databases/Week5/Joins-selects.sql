use v_art;
#1
SELECT artfile FROM v_art.artwork where period = 'Impressionism';

#2
SELECT a.artfile FROM  v_art.artwork a
inner join v_art.artwork_keyword ak on a.artwork_id = ak.artwork_id
inner join v_art.keyword k on ak.keyword_id = k.keyword_id
Where k.keyword like '%flower%';

#3
SELECT fname, lname, aw.title  FROM v_art.artist as a
LEFT JOIN v_art.artwork aw ON a.artist_id = aw.artist_id; 

#4
use magazine;
SELECT magazineName, sb.subscriberLastName, sb.subscriberFirstName
FROM magazine.magazine m
INNER JOIN magazine.subscription s ON s.magazineKey = m.magazineKey
INNER JOIN magazine.subscriber sb ON  sb.subscriberKey = s.subscriberKey
ORDER BY m.magazineName;

#5
SELECT magazineName
FROM magazine.magazine m
INNER JOIN magazine.subscription s ON s.magazineKey = m.magazineKey
INNER JOIN magazine.subscriber sb ON  sb.subscriberKey = s.subscriberKey
WHERE sb.subscriberFirstName = 'Samantha' and sb.subscriberLastName = 'Sanders'
ORDER BY m.magazineName;

#6
use employees;
SELECT e.first_name, e.last_name FROM employees.employees e
INNER JOIN dept_emp d ON e.emp_no = d.emp_no
INNER JOIN departments de ON d.dept_no = de.dept_no
WHERE de.dept_name = 'Customer Service'
ORDER BY e.last_name
LIMIT 5;

#7
SELECT e.first_name, e.last_name, de.dept_name,  s.salary, s.from_date
FROM employees.employees e
INNER JOIN salaries s ON e.emp_no = s.emp_no
INNER JOIN dept_emp d ON e.emp_no = d.emp_no
INNER JOIN departments de ON d.dept_no = de.dept_no
WHERE e.first_name = 'Berni' AND e.last_name = 'Genin'
ORDER BY s.from_date DESC
LIMIT 1;

#8
USE bike;
SELECT ROUND(AVG(quantity)) AS 'Stock Average' FROM stock;

#9
select product_name FROM product p
INNER JOIN stock s ON p.product_id = s.product_id
WHERE s.quantity = 0
ORDER BY p.product_name;

#10
SELECT category_name, SUM(quantity) FROM bike.category c
INNER JOIN product p ON p.category_id = c.category_id
INNER JOIN stock s ON s.product_id = p.product_id
WHERE s.store_id = 2
GROUP BY category_name
ORDER BY 2;

#11
use employees;
SELECT count(*) as 'Number of Employees' FROM employees.employees;

#12
	SELECT dept_name, FORMAT(average_salary,2, 'en_US') average_salary FROM (
	SELECT d.dept_name, AVG(s.salary) AS average_salary FROM departments as d
	LEFT JOIN dept_emp m ON d.dept_no = m.dept_no
	LEFT JOIN salaries s ON s. emp_no = m.emp_no
	GROUP BY d.dept_name
	) a WHERE average_salary <= 60000;

#13
SELECT de.dept_name, count(*) FROM employees.employees e
inner join dept_emp d on e.emp_no = d.emp_no
inner join departments de on d.dept_no = de.dept_no
where gender = 'F'
group by de.dept_name
order by de.dept_name;


 