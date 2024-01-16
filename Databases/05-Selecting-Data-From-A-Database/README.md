# Selecting Data From A Database

## The SELECT keyword

You use the SELECT statement to select one or more columns from a table. You can also use the SELECT statement when you want to access a subset of rows, columns, or both. When you query tables, you must include the FROM clause in your syntax. The result of the SELECT statement is called a result set. It lists rows that contain the same number of columns.

## How it works

```bash
SELECTid, name, countrycode, FROM city WHERE countrycode ='BRA’;
```

The order in which the query is processed is as follows:

1. FROMthe city table, get all data.
2. WHERE the countrycode is BRA, keep the row, and ignore the others.
3. SELECTthe specified columns (id, name, and countrycode), and ignore the others.

## Syntax

The syntax for selecting data follows a precise order. The required clauses must precede the optional clauses.

The first clause contains SELECTand the column names, and the FROMclause with the table name immediately follows it.

All optional clauses will follow these first two required clauses.

## SELECT statement considerations

- Enclose literal strings, text, and literal dates with single quotation marks (' ').
- As a best practice to improve readability, capitalize SQL keywords (for example, SELECT, FROM, and WHERE).
- Depending on the database engine or configuration,data values that you provide in conditions might be case sensitive.

## Different ways to SELECT columns

- Selecting a single column: `SELECT colname1 FROM table_name;`
- Selecting a single column and optional columns: `SELECT colname1[, colname2, colname3 ...] FROM table_name;`
- Selecting all columns: `SELECT * FROM table_name;`

## Optional clauses of the SELECT statement

`WHERE` `GROUP BY` `HAVING` `ORDER BY`

## Optional clauses of the SELECT statement: WHERE

In SQL, you can use the WHERE clause to apply a filter that selects only certain rows from a table. In a SELECT statement, the WHERE clause is optional. The SELECT-FROM-WHERE block can be useful for locating certain information in rows. You could use this construct if you needed a list of all the cities that are located within a country.

For this example, the following is the request: Get all the data from the citytable, and ignore all rows except the rows where the country code is BRA(Brazil). After you find the rows that you are searching for, return only the id, name,and countrycode columns.

The SQL query is as follows:

```bash
SELECT id, name, countrycode 
FROM city WHERE countrycode='BRA’
```

## Optional clauses of the SELECT statement: GROUP BY

```bash
SELECTcontinent, COUNT(*) FROM country GROUP BY continent;
```

Here, the SELECTstatement selects the rows from the country table, groups the rows by continent, and counts the number of rows in each group. The result is a listing of the number of countries in each continent.

Notice that the GROUP BY clause typically requires an aggregate function in the SELECT clause. In this case, the COUNT() aggregate function is used to count the number of rows in a table.

## Optional clauses of the SELECT statement: HAVING

```bash
SELECT continent, COUNT(*) FROM country 
GROUP BY continent HAVING COUNT(*) > 1;
```

The HAVING clause filters the results of a GROUP BYclause in a SELECTstatement. In this example, the query selects only the continents that have more than one country after the rows in the table are grouped by continent.

## Optional clauses of the SELECT statement: ORDER BY

```bash
SELECT id, name, countrycode FROM city ORDER BY id;
```

Use the ORDER BY clause to sort query results by one or more columns and in ascending or descending order. If the items in the table are needed in a specific order of importance, you might need to order the results in ascending or descending order.

This example makes the following request: Get all the data from the city table, and order all rows by id. After you find the rows that you are searching for, return only the id, name,and countrycode columns.

## Comment syntax

- **Single-line comment:**
  - This type of comment begins with a double dash (--).
  - Any text between the double dash and the end of the line will be ignored and not performed.
- **Inline comment:**
  - This type of comment begins with a double dash (--).
  - This comment is similar to the single-line comment in that any text between the double dash and the end of the line will be ignored and not performed. This comment differs in that it is preceded by syntax within the same line, which is not ignored.
- **Multiple-line comment:**
  - This type of comment begins with `/*` and ends with `*/`
  - Any text between the `/*` and `*/` will be ignored.
