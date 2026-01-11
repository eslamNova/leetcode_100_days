data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})



import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(right = employee, how= 'left', left_on = 'managerId', right_on= 'id')
    emp = df[df['salary_x'] > df['salary_y']]['name_x']

    return pd.DataFrame({'Employee': emp})
    