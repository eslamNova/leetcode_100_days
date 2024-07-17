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
