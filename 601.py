# https://leetcode.com/problems/human-traffic-of-stadium/description/

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium[stadium['people'] >= 100].copy()
    
    groups = []
    temp_group = []
    
    for _id, visit_date, people in stadium.itertuples(name=None, index=False):
        if temp_group and _id != temp_group[-1] + 1:
            if len(temp_group) >= 3:
                groups.extend(temp_group)
            temp_group = []
        temp_group.append(_id)
    
    if len(temp_group) >= 3:
        groups.extend(temp_group)
    
    result = stadium[stadium['id'].isin(groups)].sort_values(by='visit_date')
    
    return result
