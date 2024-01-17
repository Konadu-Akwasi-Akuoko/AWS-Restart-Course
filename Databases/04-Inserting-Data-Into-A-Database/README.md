# Inserting Data into a Database

## What is a .csv file?

A `.csv` file is a simple text file in which information is separated by commas.

- `.csv` files can be opened in any program that works with plain text.
- `.csv` files have the following format:
  - Each line contains the same sequence of data.
  - Each data point is separated by a comma. A semicolon, space, or other characters can also be used instead of a comma. However, the comma is the most common.
- These files are most commonly used to import or export data in databases and spreadsheets.

## Importing a CSV

Often, you might have a .csv file that must be imported into a database. It is straightforward to import if you follow these steps:

- Verify that the .csv file has data that matches the number of columns of the table and the type of data in each column.
- Create a table in MySQL with a table name that corresponds to the .csv file that you want to import.
- Import by using the LOAD DATAstatement.
  - If the first row of the file contains column headers, use the IGNORE 1 ROWSclause to ignore the first row.
  - If the rows in the file are terminated by a newline character, use the TERMINATED BY '\n' clause to indicate so.

This statement imports data from the temporary file into the city table:

```sql
LOAD DATA INFILE 'c:/tmp/city.csv'
INTO TABLE cityFIELDS TERMINIATED BY ' , ' 
ENCLOSED BY ' " ' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;
```

## Exporting a CSV

```sql
SELECT id, name, countrycode FROM city
INTO OUTFILE '/tmp/mysqlfiles/city.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

This statement exports data from the city table and places it into the temporary city.csv file

## Why clean data?

As changes are made to databases over time, issues can arise due to disorganization or errors in the data. Data should be cleaned for a number of reasons, but the following list contains the main reasons:

- Increased productivity
- Improved data quality
- Fewer errors

To combat these issues, data can be cleaned by using the following SQL string functions:

- **LEFT, RIGHT, and TRIM:** Use these functions to select only certain elements of strings and remove certain characters.
- **CONCAT:** Combine strings from several columns and put them together.
- **LOWER:** Force every character in a string to be lowercase.
- **UPPER:** Force every character in a string to be uppercase.

## DESCRIBE statement syntax

The `DESCRIBE` statement provides a description of the specified table or view. Usually, tables have more than one column.

To use the `INSERT` statement, it is important to know how the table that you are inserting the information into is formatted.

## INSERT INTO

The INSERT INTOstatement has the following properties:

- This statement is fundamental to populating a database table with data.
- The SQL INSERTstatement is used to insert a single record or multiple records into a table.
- The SQL INSERTstatement is referred to as a data manipulation language(DML) command.
- The order of the columns is important.

## NULL statement purpose and syntax

Null statements are used as placeholders to improve readability. They also clarify the meaning and actions of conditional statements.  

The INSERT statement can insert a NULLvalue into a column. You can insert a NULLvalue into an `int` column with a condition that the column must not have NOT NULL constraints.
