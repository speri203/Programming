!-- Query all columns for all American cities in the CITY table where population is larger than 100000. The CountryCode for America is USA
!-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
SELECT *
FROM CITY
WHERE Population > 100000
AND CountryCode='USA'
