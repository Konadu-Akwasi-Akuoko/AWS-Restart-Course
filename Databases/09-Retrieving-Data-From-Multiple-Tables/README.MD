# Retrieving Data From Multiple Tables

## Set operators

Set operators are used to combine the results of multiple queries into a single result set.

You can use different tables to compare or unite the results into one result set. Queries that contain set operations are referred to as compound queries.

| Set Operator | Use |
|--------------|-----|
| UNION        | Used to combine two or more result sets into a single set (without duplicates) |
| UNION ALL    | Used to combine two or more result sets into a single set (including duplicates) |
| INTERSECT    | Used to combine two result sets and return the data that is common in both of the result sets |
| MINUS        | Used to combine two result sets and return the data from the first result set that is not present in the second result set |

## UNION operator example

```sql
SELECT Name FROM country 
UNION
SELECT Name FROM city;
```

This query returns all the distinct country and city names in the database in one result set.

```sql
SELECT Name FROM country 
UNION ALL
SELECT Name FROM city;
```

This query returns all the country and city names in the database, including duplicates, in one result set. For example, if there is a city called Armenia (in Colombia) and a country called Armenia in the database, the result set will show Armenia twice.

## JOIN clauses defined

JOIN clauses (inner, left, right, and full joins) are used to combine rows from two or more tables.

| JOIN Clauses | Use |
|--------------|-----|
| INNER JOIN   | Return the rows that match in both tables. |
| LEFT JOIN    | Return all rows from the left table. |
| RIGHT JOIN   | Return all rows from the right table. |
| FULL JOIN    | Return all the rows from both tables. |

- Inner joins return the rows that match in both tables.
- Left joins return the rows that match in both tables and the rows from the left table that do not have a match.
- Right joins return the rows that match in both tables and rows from the right table that do not have a match.
- Full joins return the rows that match in both tables and the rows from the left and right tables that do not have a match.

## How JOIN clauses work

- **INNER JOIN:** This JOIN returns only the overlapping data between the two tables.
- **LEFT JOIN:** This JOIN returns the overlapping data between the two tables and the non-matching data from the left table.
- **RIGHT JOIN:** This JOIN is the opposite of LEFT JOIN. It returns the overlapping data between the two tables and the non-matching data from the right table.
- **FULL JOIN:** This JOIN returns the overlapping data between the two tables and the non-matching data from both the left and right tables.

The critical thing to remember is that JOINs are clauses in SQL that link two tables together. A JOINis usually based on the key or common value that defines the relationship between those two tables.

## INNER JOIN example

```sql
SELECT ci.ID AS ‘City ID’, ci.Name AS ‘City Name’, co.Name AS ‘Country Name’
FROM city ci 
JOIN country co
ON ci.CountryCode = co.Code
```

The JOINclause could be used to combine the records from the city and country table. The column names pulled from each do not need to match. For example, the JOINcolumn name is called "CountryCode" in the city table and "Code" in the country table.

In this example, the query displays the ID, name, and country name of each city in the city table

## How the INNER JOIN example works

To combine tables, each table must have related columns between them.

In the example, the CountryCode and Code columns are the commonality between the city and country tables. The two tables are joined together by combining rows whose Country Codevalue in the city table is equal to the Codevalue in the country table.

## Qualified column names

```sql
SELECT ci.ID AS ‘City ID’, ci.Name AS ‘City Name’, co.Name AS ‘Country Name’
FROM city ci
JOIN country co
ON ci.CountryCode=co.Code
```

You'll notice in this example that both tables include the Name column. When developing queries, columns with the same name in two different tables can create confusion. To avoid this confusion, use a qualifier with the column name to identify the source table.

A qualifier for a column name can be a table name, an alias name, a synonym, or a correlating name. To use a qualified column name, use the following format: `Table or alias name.column name`
