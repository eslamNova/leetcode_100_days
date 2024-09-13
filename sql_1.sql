Select Product_id from products Where low_fats = 'Y' and recyclable = 'Y'

Select name from Customer where referee_id != 2 or referee_id is null

Select name, area, population from World WHERE area >= 3000000 or population >= 25000000

Select DISTINCT author_id as id from Views WHERE author_id = viewer_id ORDER BY id

SELECT tweet_id from Tweets WHERE length(content) > 15

Select eu.unique_id AS unique_id, e.name from Employees e Left Join EmployeeUNI eu USING(id)

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    s_p = sales.merge(product, on=["product_id"])

    df = s_p[['product_name', 'year', 'price']]

    return df

Select p.product_name, s.year, s.price from Sales s Join product p ON s.product_id = p.product_id


Select w1.id From Weather w1 Join Weather w2 On DATEDIFF(w1.recordDate, w2.recordDate) = 1 WHERE w1.temperature > w2.temperature

Select e.name, b.bonus from Employee e LEFT JOIN Bonus b ON e.empId = b.empId WHERE bonus < 1000 or bonus is NULL

SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
    

SELECT teacher_id, count(distinct subject_id) as cnt from Teacher group by teacher_id


Select class from Courses Group By class Having COUNT(student) >= 5

Select * from Cinema Where MOD(id, 2) = 1 AND description != 'boring' ORDER BY rating DESC;

Select activity_date AS day, COUNT(DISTINCT user_id) AS active_users FROM Activity WHERE DATEDIFF('2019-07-27', activity_date) < 30 AND DATEDIFF('2019-07-27', activity_date) >= 0 GROUP BY 1


SELECT Users.user_id , CONCAT(UPPER(SUBSTR(Users.name,1,1)),LOWER(SUBSTR(Users.name,2))) AS name 
FROM Users
ORDER BY
Users.user_id ASC

Select employee_id FROM Employees Where salary < 30000 AND manager_id NOT IN (Select employee_id From Employees) order by employee_id;


Select FirstName, LastName, City, State from Person left join Address on Person.PersonId = Address.PersonId ;

<<<<<<< HEAD

Select * From patients Where conditions REGEXP  '\\bDIAB1'

a
=======
Select employee_id, department_id From Employee WHERE primary_flag = "Y" UNION Select employee_id, department_id From Employee GROUP BY employee_id Having COUNT(employee_id) = 1


Select project_id, ROUND(AVG(experience_years), 2) AS average_years From Project p Join Employee e On p.employee_id = e.employee_id Group By project_id
>>>>>>> 78a7d953cb8bd57b6289819cb6fe0fb3fef945b0
