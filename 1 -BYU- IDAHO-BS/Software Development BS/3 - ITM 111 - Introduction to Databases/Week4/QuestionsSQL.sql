use v_art;
#Question - 1
INSERT INTO v_art.artist (fname, mname, lname, dob, dod, country, local)
VALUES('Johannes','', 'Vermeer', 1632, 1674, 'Netherlands', 'n');

#Question - 2
SELECT fname, mname, lname, dob, dod, country, local, artist_id 'Artist ID TO EDIT or DELETE' FROM v_art.artist ORDER BY lname ASC;

#Question - 3
SELECT @ID := artist_id FROM v_art.artist Where fname = 'Johannes' and lname = 'Vermeer';
UPDATE v_art.artist SET dod = 1675 WHERE artist_id = @ID;

#Question - 4
SELECT @ID := artist_id FROM v_art.artist Where fname = 'Johannes' and lname = 'Vermeer';
DELETE FROM v_art.artist WHERE artist_id = @ID;

#Question - 5
USE bike;
SELECT first_name, last_name, phone FROM customer WHERE city = 'Houston';

#Question - 6
SELECT product_name, list_price, list_price - 500 AS 'Discount Price'  FROM product WHERE list_price > 5000 ORDER BY list_price DESC;

#Question - 7
SELECT first_name, last_name, email FROM staff WHERE store_id <> 1;

#Question - 8
SELECT product_name, model_year, list_price  FROM product WHERE product_name LIKE '%spider%';

#Question - 9
SELECT product_name, list_price  FROM product WHERE list_price BETWEEN 500 AND 550 ORDER BY list_price ASC;

#Question - 10
SELECT first_name, last_name, phone, street, city, state, zip_code FROM customer 
WHERE phone IS NOT NULL 
AND city LIKE '%ach%' OR city LIKE '%och%'
OR last_name = 'William';

#Question - 11
SELECT SUBSTRING(product_name, 1, LOCATE( '-', product_name)-1) AS 'Product name without year'
 FROM product
ORDER BY product_id
LIMIT 14;

#Question - 12
SELECT product_name, CONCAT('$', FORMAT(list_price /3,2, 'en_US')) 'One of 3 payments' FROM product
WHERE model_year = 2019;

#Question - 13
USE magazine;
SELECT magazineName, magazinePrice, ROUND(magazinePrice - (magazinePrice * 0.03), 2) FROM magazine;

#Question - 14
SELECT sr.subscriberKey ,
 CEILING(DATEDIFF('2020-12-20', SB.subscriptionStartDate) /365) AS 'Years since subscription'
FROM subscriber sr
INNER JOIN subscription sb
ON sr.subscriberKey = sb.subscriberKey;

#Question - 15
SELECT sb.subscriptionStartDate, sb.subscriptionLength,
 DATE_FORMAT(DATE_ADD(SB.subscriptionStartDate, INTERVAL sb.subscriptionLength MONTH), '%M %e, %Y') AS 'Subscription End'
FROM subscription sb;