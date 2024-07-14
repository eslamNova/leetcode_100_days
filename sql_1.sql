Select Product_id from products Where low_fats = 'Y' and recyclable = 'Y'

Select name from Customer where referee_id != 2 or referee_id is null

Select name, area, population from World WHERE area >= 3000000 or population >= 25000000

Select eu.unique_id AS unique_id, e.name from Employees e Left Join EmployeeUNI eu USING(id)
