# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee['managerId'] = employee['managerId'].fillna(employee['id'])

    manager_counts = employee['managerId'].value_counts()
    masters = manager_counts[manager_counts > 4].index

    if not len(masters):
        return pd.DataFrame(columns=['name'])

    return pd.DataFrame({'name': employee.loc[employee['id'].isin(masters), 'name']})
