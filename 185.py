# https://leetcode.com/problems/department-top-three-salaries/

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    department = department.rename(columns={'id': 'departmentId', 'name': 'Department'})

    df = employee.merge(department, on=['departmentId'], how='left')

    df['rank'] = df.groupby(['departmentId'])['Salary'].rank(ascending=False, method='dense')

    df = df[df['rank'] <= 3]

    return df[['Department','Employee', 'Salary']]
