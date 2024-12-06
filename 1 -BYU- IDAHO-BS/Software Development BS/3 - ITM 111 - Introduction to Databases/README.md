### Terms to Know

Familiarize yourself with the following terms.

**Data**:
 - The bits and pieces, like numbers, characters or symbols with no relevance.

**Information:**
- A set of data with relevance. At a certain place in time, or for a certain person, the data makes sense.

**Knowledge:**

- Information that has been acquired and gives understanding about the importance of the information. Used to make decisions.

**Decision-making:**

- Acting on the knowledge obtained, to achieve some benefit.

**Entity:**

- A person, place, thing or concept about which data can be collected.

**Attribute:**

- Describes the facts, details or characteristics of an entity.

**Data–driven Decision–Making:**

- Using data as the basis for making decisions in an organization to avoid bias and false assumptions that lead to poor decisions.

**Query:**

- A request for data or information. Asking a question from the data.

**Sort:**

- Arrange data or information in a specific way to make it more useful. Such as alphabetizing from A to Z.

**Filter**:

- Hiding or filtering out unwanted data or information so only the information you want to see is displayed.

**Statement of Work (SOW):**

- A document used to plan a successful execution of a project or system. Used in planning for data systems such as databases.

**Data Integrity:**

- Ensuring the accuracy and reliability of data, making sure it remains intact. It can be maintained by standards implemented during the design phase.

**Data Consistency:**

- The usability of data, or having only valid data written to the database. All values in a single attribute of an entity should be of the same data type.

**Data Redundancy:**

- The repetition of data where the same data value is stored in more than one place in the database. This wastes space and necessitates multiple changes in different places when editing the value.

**Entity Data Storage:**

- A single thing, person, place, or object; usually represented as a single row in data storage. Also referred to as a record.

**Attribute Data Storage:**

- A value that describes a characteristics of the entity. A set of these related values for many entities are represented as a column in data storage. Also referred to as a field.

--Week2--

**Datatype:**
- A particular kind of data item, as defined by the values it can take.

**Data Model:**
- Determines the logical structure of a database and determines in which manner data can be stored, organized, and manipulated.

**Hierarchical Model:**
- Organizes data in a tree-like structure with parents and child nodes. Each child node will only have one parent node. Parents can have many child nodes.

**Network Model:**
- An extension of the hierarchical database model. With the network model, child nodes can have more than one parent, allowing more flexibility.

**Relational Model:**
- The most common model that organizes data in rows and tables, which in turn can be accessed and linked to other rows and tables by sharing a common field.

**Object-Oriented Model:**
- Represents data as an object with properties and methods and combines database capabilities with object-oriented programming language capabilities.

**NoSQL:**
- An unstructured database model that can store virtually any structure where new columns can be created easily.

**Edgar F. Codd:**
- A computer scientist who invented the relational model for database management, the theoretical basis for relational databases and relational database management systems.

**SQL:**
- Structured Query Language, the language to communicate with a database.

**MySQL:**
- The most popular open-source relational database management system.

**MySQL Workbench:**
- A visual tool for database providing data modeling, SQL development, administration tools, user administration, and backups.

**Table:**
- A part of a database that represents one real world entity or one group of related instances of that entity. Each row of a table is one instance of the entity. Each column an attribute of that entity.

**Primary Key:**
- An attribute (or group of attributes) that uniquely identifies a given entity in a table.

**Foreign Key:**
- A primary key of one table that appears as an attribute in another table and acts to provide a logical relationship between the two tables. Foreign keys can repeat.

**Referential Integrity:**
- A rule that prevents invalid relationships between tables when changes are made to the data.

**Null:**
- A term stating that an attribute value doesn't have to exist. In other words, the user can leave the value blank.

**Auto-increment:**
- A table column which produces a sequential system-generated number when a new record is inserted into a table.

**Surrogate Key:**
- A system-assigned primary key, generally numeric and auto-incremented.

**Composite Key:**
- Two or more attributes that together define the primary key by unique combinations of their values.

**Natural Key:**
- A key that naturally occurs in the attributes of an entity, such as a student ID or a course name.

**ERD (Entity Relationship Diagram):**
- A diagram that shows how database tables are defined and relate.

**Cardinality (Entity Relationships):**
- How the occurrences in one entity are linked to the number of occurrences in another entity (one-to-one, one-to-many, and many-to-many).

**Crows feet notation:**
- A way to symbolize relationships between tables in an entity relationships diagram (ERD).

**Primary Key:**
- Uniquely identifies each row in a table. It can't be repeated as a primary key.

**Foreign Key:**
- Shows a relationship to a primary key of another table. It could possibly be repeated as a foreign key depending on the relationship.

**Composite Key:**
- When two or more columns are used to uniquely identify a row in a table.

**Natural Key:**
- Uniquely identifies a single record or row in a table and is made up of real data (data that has meaning and occurs naturally in the real world).

**Surrogate Key:**
- Uniquely identifies a single record or row in a table but doesn't have a natural relationship with the rest of the columns in the table. They can be created with auto-incrementing.

**DDL - Data Definition Language**
- DDL Statement has to do with the Structure of the Database. Like Create Table, Create Database ...

**DML - Data Manipulation Language**
- DML Statement has to do with the data manipulation of the Database, the data itself. Like Insert int "Table" Values (1, "teste)
**Database design:**
- Organizing data to minimize redundancy and ensure data integrity and consistency.

**Normal Forms:**
- A set of rules that if applied to data reduces data redundancy and attributes of each entity are organized in a way that increases data integrity and consistency.

**First Normal Form (1NF):**
- Each cell of the table should only have one single (scalar) value and there should be no repeating columns. 
The table should also have a primary key.

**Second Normal Form (2NF):**
- Every non-key column must depend on the entire primary key (both parts of a composite primary key).

**Third Normal Form (3NF):**
- Every non-key column must depend only on the primary key (a single value primary key).

**De-normalizing:**
- Ignoring some normal forms if it improves performance of a database.

**Following the Normal Form objective**
- By following normalization rules (or normal forms) we reduce data redundancy. The attributes of each entity are organized in a way that increases data consistency.

**CRUD (Create, Read, Update and Delete):**
- These are the four basic functions of relational databases.

**DDL (Data Definition Language):**
- SQL commands that are used to define the database, to create and modify the actual structure of the database. Examples are CREATE, ALTER and DROP.

**DML (Data Manipulation Language):**
- SQL commands that deal with manipulating data in the database. Examples are INSERT, UPDATE, and DELETE.

**CREATE:**
- SQL command that will create new schemas, databases or tables.

**INSERT:**
- SQL commands to add data into tables.

**UPDATE:**
- SQL command to modify or edit data in tables. Always use a WHERE clause with UPDATE.

**DELETE:**
- SQL command to delete data in tables. Always use a WHERE clause with DELETE.

**DROP:**
- SQL command to delete not only data in the table but the table definition itself. So, the entire table is completely deleted.

**Referential Integrity:**
- Implies that relationships among data should be enforced to guarantee the relationship between rows in two tables will remain synchronized during all updates and deletes.

**Foreign Key Constraints:**
- Enforces referential integrity by guaranteeing that changes cannot be made to data in the primary table if those changes invalidate the link to data in the foreign key table.

### QUESTIONS

## BIG Data
**What types of data about you is stored in databases?**
- I believe it depends on the kind of service but usually Name, address, age, phone number, etc.

**What type of data do companies like Amazon, Instagram, and Google store about you?**
- Personal data like name, phone number, email, person related with, liked publications, photos, publications.

**What is SQL**
- SQL, or Structured Query Language, is a specialized programming language designed for managing, manipulating, and retrieving data stored in relational databases.

**Syntax vs. Semantics**
- Each SQL Statement has syntactic and semantic component.
 In SQL, the distinction between syntax and semantics is crucial for understanding and effectively using the language.

 - Syntax refers to the rules governing the structure and grammar of SQL statements, determining whether a query is written correctly according to the language's conventions.
 - Semantics pertain to the meaning and interpretation of SQL statements, determining the behavior of queries and their effects on the database. Semantics encompass concepts such as data retrieval, manipulation, transaction management, and integrity constraints, ensuring that queries are executed correctly and produce the desired results. While syntax errors can be detected by the SQL parser, semantic errors—such as querying for data that doesn't exist or unintentionally modifying data—require a deeper understanding of SQL's functionality and the underlying database schema to identify and rectify effectively.

 **SQL Statement**
 - A SQL statement is a command used to perform a specific action on a database.

 -SQL statements can be categorized into several types, including:
    - Data Manipulation Language (DML) statements like SELECT, INSERT, UPDATE, and DELETE
        - which are used to retrieve, add, modify, and remove data from tables respectively.
    - Data Definition Language (DDL) statements like CREATE, ALTER, and DROP
        - which are used to define, modify, and delete database objects such as tables, indexes, and views.

**Parts of a SQL Statement**
SQL statements are made up of several parts. The basic parts are:

Clause: A clause is a component of a SQL statement that specifies a particular action to be performed. Common clauses include SELECT, INSERT, UPDATE, DELETE, WHERE, GROUP BY, HAVING, ORDER BY, JOIN, CREATE, ALTER and DROP.
Keywords: Keywords are reserved words in SQL that have special meanings. These include commands like SELECT, INSERT, UPDATE, DELETE, WHERE, FROM, JOIN, and others. Keywords are used to define the type of operation to be performed or to specify conditions.
Expressions: Expressions are combinations of literals (and exact number, or text), column names, operators, and functions that evaluate to a single value. They can be used to define calculations, conditions, or values to be returned in a query.
Identifiers: Identifiers are names given to database objects such as tables, columns, indexes, and constraints. They must adhere to certain rules depending on the database system used, such as being enclosed in quotes or adhering to specific naming conventions.
Operators: Operators are symbols or keywords used to perform comparisons or operations in SQL statements. Common operators include arithmetic operators

```SQL

Example Statement
Let's look at the SQL statement

SELECT name, age FROM student WHERE student_id = 2983756;
//The previous statement consist of

//Keywords: SELECT, FROM, WHERE
//Identifiers: name, age, student, student_id
//Operator: =Number literal: 2983756 (note: text literals must be enclosed in quotes e.g. 'this is a text literal')
//; (semicolon): Statement terminator

```

**SELECT:**  
- A statement that describes the columns in the result set, used to retrieve table data.  

**FROM:**  
- A command that indicates the table you are getting data from.  

**ORDER BY:**  
- A keyword used to sort the rows of a result set.  

**LIMIT:**  
- A clause used to show the number of rows to return in the result set.  

**DISTINCT:**  
- A keyword used to eliminate duplicate rows in the result set.  

**WHERE:**  
- A clause used to retrieve just the data you want; filters the data.  

**Arithmetic Operators:**  
- Used to make calculations. Examples are multiplication (*), division (/), modulus (%), addition (+), and subtraction (-).  

**Comparison Operators:**  
- Used to make comparisons to restrict information in the result set. Examples are equal to (=), less than (<), less than or equal to (<=), greater than (>), greater than or equal to (>=), and not equal to (<> or !=).  

**Logical Operators:**  
- Use with multiple conditions to combine or negate search conditions. Examples are both conditions have to be true (AND), one of the conditions has to be true (OR), and negates the condition (NOT).  

**IN:**  
- An operator that can test an expression to a list of expressions.  

**BETWEEN:**  
- An operator that can compare an expression with a range of values.  

**LIKE:**  
- Operator that matches string patterns to a test expression letting you filter the results according to certain string patterns.  

**REGEXP:**  
- A regular expressions operator that allows much more complex string patterns to test expressions.  

**Null Value:**  
- No value, blank. It is different from a zero value or a field that contains spaces; null values have been left blank when the row was added.  

**IS NULL (IS NOT NULL):**  
- Constraints to test for null values. IS NULL for all nulls. IS NOT NULL for all that are not nulls.  

**ASC:**  
- Keyword used with ORDER BY to sort the results in ascending order (smallest to largest).  

**DESC:**  
- Keyword used with ORDER BY to sort the results in descending order (largest to smallest).  

**Order of Execution:**  
- The order the system actually executes clauses. This is a different order from how the clauses are written in SQL code.  

**Function:**  
- A stored program or operation that, when performed on data, returns a value or manipulates or converts the data.  

**Scalar Function:**  
- A function that works on a single entity of data, not a group of data together.  

**Parameter:**  
- Used to pass data values to a function. SQL function parameters are inside parentheses following the function name, and if there is more than one parameter, they are separated by a comma.  

**Concatenate:**  
- Combining values, by appending them to each other, to form a single longer value.  

**Index numbering:**  
- The number related to each character of a string. SQL index numbering starts at 1 for the first character.  

### Commonly used Text-manipulation or String Functions
Function	                        Description
CONCAT(string, string)	            Returns all the string combined into one string
LEFT(string, length)	            Returns characters from the left of the string
RIGHT(string, length)	            Returns characters from the right of the string
LTRIM(string)	                    Trims white space from the left of the string
RTRIM(string)	                    Trims white space from the right of the string
TRIM( string)	                    Trims white space from the left and right of the string
LENGTH(string)	                    Returns the length of characters of the string
LOWER(string)	                    Converts the string to lowercase
UPPER(string)	                    Converts the string to uppercase
LOCATE(find, search, start)	        Find a substring within the string
SUBSTRING(string, start, length )	Return characters from within a string
SUM([ALL| DISTINCT] expression)     Returns the sum of a column's values
MAX([ALL| DISTINCT] expression)     Returns a column's highest value
MIN([ALL| DISTINCT] expression)     Returns a column's lowest value
COUNT([ALL| DISTINCT] expression)   Returns the number of rows in a column
AVG([ALL| DISTINCT] expression)     Returns a column's average value


### Commonly used Numeric Functions

Function	                        Description
ROUND(number, length)	            Returns the number rounded
FLOOR(number)	                    Returns the next smaller whole number
CEILING(number)	                    Returns the next larger whole number
ABS(number)	                        Returns the absolute value of the number
SQRT(number)	                    Returns the square root of the number
MOD(number, divisor)	            Returns the remainder of the number divided by the divisor
FORMAT(number, decimals, locale)	Returns the number is currency format


### Commonly used Date and Time Functions
Function	                            Description
YEAR(date)	                            Returns the year portion of a date
MONTH(date)	                            Returns the month portion of a date
DAY(date)	                            Returns the day portion of a date
HOUR(time)	                            Returns the hour portion of a time
MINUTE(time)	                        Returns the minute portion of a time
SECOND(time)	                        Returns the second portion of a time
NOW()	                                Returns the current local time and date from your system
DATE_ADD(date, INTERVAL length time)	Adds a specified interval to a date
DATEDIFF(date, date)	                Calculates the difference in days between two dates
DATE_FORMAT(date, format)	            Returns a string for a date with specific formatting

### Codes for DATE_FORMAT Function
Format Code	Description
%c	        Month, numeric
%M	        Month name
%e	        Day of the month, numeric
%D	        Day of the month with suffix
%y	        Year, 2 digits
%Y	        Year, 4 digits
%W	        Weekday name

### * The order in which the computer actually executes the clauses is different. This is referred to as the Order of Execution.
FROM
WHERE
SELECT
ORDER BY
LIMIT


## JOINS
INNER JOIN       
    Returns rows that have matching values in both tables	
LEFT JOIN        
    Returns all rows from the left table, and matched rows from the right table
RIGHT JOIN       
    Returns all rows from the right table, and matching rows from the left table
FULL OUTER JOIN  
    Returns all rows from both tables, even if there is not a related key

**Order of System Execution**
1. FROM and JOIN
2. WHERE
3. SELECT
4. ORDER 

**SELECT Order of Execution**
- The written order, or the syntax order of how we write a query differs from the order of how the query is actually executed. It's important to understand the order of execution so you know what results are accessible where.

FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT


```SQL
--The ALL keyword is assumed with aggregate functions. You don't have to include it. This means all rows are included in the aggregate function, which is the default.


SELECT AVG(ALL prod_price) AS 'Average Price'
FROM products
--All product prices are included in the average calculation.

---You can use the DISTINCT keyword instead to include only unique values.

SELECT AVG(DISTINCT prod_price) AS 'Average Price'
FROM products
--So if there are multiple products with the same price, that price will only be included once in the average calculation.
```

- The ROLLUP operator can be used with grouping and aggregates allowing you to add one or more summary rows to your results. A summary row will show up for every group you have.

```SQL
SELECT vendor_id, SUM(product_price) AS 'Total of Product Prices'
FROM products
WHERE vendor_id < 15
GROUP BY vendor_id WITH ROLLUP

vendor_id	Total of Product Prices
010	        121.87
011	        242.21
012	        450.43
013	        312.12
014	        576.94
NULL	    1703.57 --this line is because the WITH ROLLUP
--The summary row shows up as the bottom row and totals all the totals into a grand total.
```