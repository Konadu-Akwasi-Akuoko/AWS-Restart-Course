# Working With Functions

## Built-in functions

Some common functions include aggregate functions, conversion functions, date functions, string functions, mathematical functions, and control flow and window functions.

## Built-in functions: Example syntax

- The `CURRENT_DATE()` function returns the current date as a value in ‘YYYY-MM-DD’ format.
- The `DATE_ADD()` function adds a time or date interval to a date and returns a value.

## Common aggregate functions

| Aggregate Function | Use Case and Example |
|--------------------|----------------------|
| AVG                | - Returns the average of a set <br> - Can be used to find the average population for cities within a specified country |
| COUNT              | - Returns the number of items in a set <br> - Can be used to find the total number of cities listed within a specified country |
| MAX                | - Returns the maximum value in a set <br> - Can be used to find the city with the greatest number or highest population |
| MIN                | - Returns the minimum value in a set <br> - Can be used to find the city with smallest number or lowest population |
| SUM                | - Returns total of all values in a set <br> - Can be used to find total population for all cities that are listed for specified country |

## Aggregate functions: Example syntax

```sql
SELECT COUNT(*) AS ‘Total Number of Rows’ FROM countrylanguage;

ELECT AVG(LifeExpectancy) FROM country;
```

## DISTINCT (different) keyword

```sql
SELECT DISTINCT CountryCode, District FROM city;
```

## DISTINCT in a COUNT function

```sql
SELECT COUNT(DISTINCTCountryCode) AS Unique_Country_Codes FROM city;
```

## String function: CHAR_LENGTH()

```sql
SELECT CHAR_LENGTH('District');
```

## String function: INSERT()

```sql
SELECT INSERT ("Population", 1, 2, “Mani”);
```

## Leading and trailing spaces in a string

Extra spaces in a string can cause issues when querying for specific data.

## TRIM functions: RTRIM() and LTRIM()

```sql
SELECT ID, RTRIM(District) AS District FROM city;
```

- The RTRIM() function removes blank spaces to the right of a string.
- The LTRIM() function removes blank spaces to the left of a string.
