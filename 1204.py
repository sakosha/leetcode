# https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by=['turn'])

    capacity = 1000
    last_person = None
    total_weight = 0

    for person_name, weight in zip(queue['person_name'], queue['weight']):
        if total_weight + weight <= capacity:
            total_weight += weight
            last_person = person_name
            continue
        break

    if last_person is None:
       return pd.DataFrame(columns=['person_name'])

    return pd.DataFrame({'person_name': [last_person]})
