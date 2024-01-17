# Organizing Data

## Organizing data by using SQL

- Sorting is the practice of organizing the sequence of the data returned by a query so that the data can be analyzed effectively.
- Structured query language (SQL) statements use the ORDER BY clause to sort query output in a specified order.
- Query output can be sorted in either ascending or descending order.
- SQL statements use the GROUP BY clause to combine query output into groups.
- SQL statements use the HAVING clause to apply filter conditions to aggregated group data.

## Query output with no sorting

```sql
SELECTname, continent, surfacearea
FROM country
WHERE surfacearea >= 5000000;
```

This query does not include any SQL clauses for sorting. Therefore, the data is returned in no specific order. Some SQL databases return the rows in the order in which they were originally loaded into the table.

## Query output sorted in ascending order

```sql
SELECTname, continent, surfacearea 
FROM country 
WHERE surfacearea >= 5000000
ORDER BY surfacearea ASC;
```

This query includes an ORDER BY clause, which sorts the query results in a specific order. In this case, it orders by the values of the surfacearea column from smallest to largest. Ordering data from smallest to largest value is referred to as ascending order.

Ascending order sorts are specified by including the ASC keyword, which follows the ORDER BY clause. Because ascending order sorts are the default sort order for an ORDER BY clause, omitting the ASC keyword will still provide the same results.

## Query output sorted in descending order

```sql
SELECTname, continent, surfacearea 
FROM country 
WHERE surfacearea >= 5000000
ORDER BY surfacearea DESC;
```

This query also includes a SQL clause with an ORDER BY clause. This time the query results are sorted by the values of the surfacearea column from largest to smallest.  Ordering data from largest to smallest values is referred to as descending order.

Descending sorts are specified by including the DESC keyword, which follows the ORDER BY clause.

## Query output by using multiple sort operations

```sql
SELECTname, continent, surfacearea
FROM country 
WHERE surfacearea >= 5000000
ORDER BY continent ASC, surfacearea DESC;
```

## Query output by using implicit columns in sort operations

```sql
SELECT name, continent, surfacearea
FROM country WHERE surfacearea >= 5000000
ORDER BY 2 ASC, 3 DESC;
```

Instead of spelling out entire column names in an ORDER BY clause, you can also use implicit column placeholders.

This query has continent and surfacearea columns as the second and third columns in the SELECT clause.

You can use those implicit numeric placeholder values in the ORDER BY clause in place of the actual column names themselves. In this example, the number 2 in the ORDER BY clause represents the continent column from the SELECT clause. The number 3 represents the surfacearea column from the SELECT clause.

## Grouping data in query output

```sql
SELECT continent, name
FROM country
WHERE(continent = 'South America' AND population > 12000000)
OR continent = 'Antarctica'ORDER BY 1, 2;
```

This query returns the continent and name of each country that has one of the following characteristics:

- The country is in South America and has a population of more than 12 million people.
- The country is on the continent of Antarctica.

The results are ordered by country name within continent.

## Grouping data in query output by using GROUP BY

```sql
SELECT continent, COUNT(name) AS 'countries'
FROM country
WHERE(continent = 'South America' AND population > 12000000)
OR continent = 'Antarctica' GROUP BY continent ORDER BY 1, 2;
```

In this example, the GROUP BY clause groups together all the data items that have the same value for continent name. Then, it counts how many country names are included in that group.

You can use the GROUP BY clause in a SQL statement to group data items of the same value together.

The GROUP BY clause is typically used in conjunction with SELECT statements that include SQL aggregation functions such as COUNT, MAX , MIN, SUM, and AVG.

The GROUP BY clause groups the query results together by using the specified aggregation function.

## Using GROUP BY items with filter conditions

- SQL statement WHERE clauses are evaluated before the GROUP BY clause.
- The HAVING clause is used to filter query results after applying the GROUP BY clause.
- The HAVING clause will include the same column used in the aggregation function of the SELECT clause.

## Adding the HAVING clause as filter condition

```sql
SELECT continent, COUNT(name) AS 'countries' 
FROM country WHERE(continent = 'South America' AND population > 12000000)
OR continent = 'Antarctica' GROUP BY continent
HAVING COUNT(name) > 5 ORDER BY 1, 2;
```

The HAVING clause in a SQL statement is used with the GROUP BY clause to add a filter condition based on the aggregated value.

In this example, the GROUP BY clause returns two rows. The HAVING clause then further filters those rows to return only the continents that have more than five countries in them.


