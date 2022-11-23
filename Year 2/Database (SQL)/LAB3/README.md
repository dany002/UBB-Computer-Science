Lab 3. Altering the Database

assigned: week 6; due: week 8
Sometimes, after you design a database, you need to change its structure. Unfortunately, changes aren’t correct every time, so they must be reverted. Your task is to create a versioning mechanism that allows you to easily switch between database versions.

Write SQL scripts that:
a. modify the type of a column;
b. add / remove a column;
c. add / remove a DEFAULT constraint;
d. add / remove a primary key;
e. add / remove a candidate key;
f. add / remove a foreign key;
g. create / drop a table.

For each of the scripts above, write another one that reverts the operation. Place each script in a stored procedure. Use a simple, intuitive naming convention.

Create a new table that holds the current version of the database schema. Simplifying assumption: the version is an integer number.

Write a stored procedure that receives as a parameter a version number and brings the database to that version.

Useful references:

seminars 1, 3
T-SQL
DECLARE, SET, BEGIN…END
http://msdn.microsoft.com/en-us/library/ms188927.aspx
http://msdn.microsoft.com/en-us/library/ms189484.aspx
http://msdn.microsoft.com/en-us/library/ms190487.aspx
WHILE
http://msdn.microsoft.com/en-us/library/ms178642.aspx
sp_executesql
http://msdn.microsoft.com/en-us/library/ms188001.aspx
Stored Procedures
http://msdn.microsoft.com/en-us/library/ms190782.aspx
SQL Server technical documentation
https://docs.microsoft.com/en-us/sql/sql-server/sql-server-technical-documentation
