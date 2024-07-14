Select Product_id from products Where low_fats = 'Y' and recyclable = 'Y'

Select name from Customer where referee_id != 2 or referee_id is null

Select name, area, population from World WHERE area >= 3000000 or population >= 25000000

Select DISTINCT author_id as id from Views WHERE author_id = viewer_id ORDER BY id

SELECT tweet_id from Tweets WHERE length(content) > 15

Select eu.unique_id AS unique_id, e.name from Employees e Left Join EmployeeUNI eu USING(id)
