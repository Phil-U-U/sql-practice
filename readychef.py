
# readychef
# Aggregation Functions
# Q8:
# Maybe you only want to consider the meals which occur in the first quarter (January through March).
# Use date_part to get the month like this: date_part('month', dt).
# Add a WHERE clause to the above query to consider only meals in the first quarter of 2013 (month<=3 and year=2013).

Select
    type, min(price) as min_price, max(price) as max_price
From meals
Where
    date_part('year', dt) = 2013 and date_part('month', dt) <= 3
Group by type;



SELECT
    type,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM meals
WHERE
    date_part('year', dt)=2013 AND
    date_part('month', dt)<=3
GROUP BY type;


# Q9:
# Modify the above query so that we get the aggregate values for each month and type.
Select
    date_part('month', dt) as Month,
    type,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
From meals
Where
    date_part('year', dt) <= 2013 and
    date_part('month', dt) <= 3
Group by type, Month
Order by Month;


SELECT
    type,
    date_part('month', dt) AS month,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM meals
WHERE
    date_part('year', dt)=2013 AND
    date_part('month', dt)<=3
GROUP BY type, month;


# Q 10:
# From the events table, write a query that gets the total number of buys, likes and shares for each meal id.
# Extra: To avoid having to do this as three separate queries you can do the count of the number of buys like this:
# SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END).
SELECT
    meal_id,
    SUM( CASE WHEN event = 'bought' THEN 1 ELSE 0 END) as buys,
    SUM( CASE WHEN event = 'like' THEN 1 ELSE 0 END) as likes,
    SUM( CASE WHEN event = 'share' THEN 1 ELSE 0 END) as shares
FROM events
GROUP BY meal_id
LIMIT 10;

SELECT
    meal_id,
    SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END) AS bought,
    SUM(CASE WHEN event='like' THEN 1 ELSE 0 END) AS liked,
    SUM(CASE WHEN event='share' THEN 1 ELSE 0 END) AS shared
FROM events
GROUP BY meal_id;


# to be continued: sorting
