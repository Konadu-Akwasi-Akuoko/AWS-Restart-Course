# Performing A Conditional Search

## Overview of search conditions

The SELECT statement has five main clauses:

- FROM clause (required)
- WHERE clause
- GROUP BY clause
- HAVING clause
- ORDER BY clause

The WHERE clause is used to filter the data that the query returns.

The WHERE clause sets up a search condition that uses a logical test to decide whether a row should be included in a query.

Search conditions compare two values by using an operator to test whether the search condition is met.

If the search condition is met, the query returns the data items from the table.

## Search condition in a WHERE clause

```sql
SELECT continent, surfacearea, population, gnp FROM country WHERE name = 'Ireland’
```

The example shows a conditional search that uses the WHERE clause with the equal to (=) comparison operator.

Specifically, this query returns the continent, surface area, population, and gross national product (GNP) data for the country named Ireland.

## Types of operators

1. Arithmetic operators perform mathematical operations.
2. Comparison operators compare values between data items.
3. Logical operators are used to build compound conditions

These operators can be used in SELECT, INSERT, UPDATE, and DELETE statements.

## Arithmetic operators

| SQL operation          | SQL operator |
|------------------------|--------------|
| Addition               | +            |
| Subtraction            | -            |
| Multiplication         | *            |
| Division               | /            |
| Modulus (remainder)    | %            |

## Comparison operators

| SQL operation | Operation             | Description                                                           |
|---------------|-----------------------|-----------------------------------------------------------------------|
| =             | Equals                | Compares two data items to see whether they are equal                 |
| !=, <>        | Not equal             | Compares two data items to see whether they are not equal             |
| <             | Less than             | Compares two data items to see whether the value of the data item on the left is less than the value on the right |
| <=            | Greater than          | Compares two data items to see whether the value of the data item on the left is less than or equal to the value on the right |
| >             | Greater than          | Compares two data items to see whether the value of  the data item on  the left is greater than  the value on  the right |
| >=            | Greater than or equal | Compares two data items to see whether  the value of  the data item on  the left is greater than or equal to  the value on  the right |

## Addition arithmetic operator

```sql
SELECTname, lifeexpectancy, lifeexpectancy + 5.5 FROM country WHERE gnp > 1300000;
```

Suppose research shows that the average life expectancy is expected to increase by 5.5 years for countries whose GNP is greater than $1.3 trillion.

This query calculates the new life expectancy for these countries. It adds 5.5 to the current value for life expectancy and then displays that calculated value in the query result.

## Subtraction arithmetic operator

```sql
SELECT name, continent, population, population-350000
FROM country
WHERE name='United States';
```

Suppose research shows that the United States population is expected to decline by 350,000 people due to lower birth rates and emigration to other countries.

This query calculates that the new population of the United States will be 278,007,000 people following that decline. It displays that calculated value in the query result.

## Multiplication arithmetic operator

```sql
SELECT name, continent, population, population*1.15
FROM country 
WHERE name = 'Malta';
```

Suppose research shows that Malta expects a 15 percent increase in population as people from around the world move there to live following their retirement.

This query calculates the new population for Malta by multiplying the current value for population by 1.15. It then displays that calculated value in the query result.

## Division arithmetic operator

```sql
SELECT name, region, population, surfacearea, population/surfacearea
FROM country
WHERE population/surfacearea > 3000;
```
