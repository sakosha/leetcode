# https://leetcode.com/problems/trips-and-users/description/

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    users = users.loc[users['banned'] == 'No']
    trips = trips.loc[trips['client_id'].isin(users['users_id'])]
    trips = trips.loc[trips['driver_id'].isin(users['users_id'])]
    trips = trips.rename(columns={'request_at': 'Day'})

    grouped = trips.groupby('Day')['status'].value_counts().unstack(fill_value=0)

    grouped['Cancellation Rate'] = 1 - (grouped.get('completed', 0) / grouped.sum(axis=1))
    df = grouped[['Cancellation Rate']].reset_index()

    # if len(df.index) == 1:
    #     df = df.loc[df['Cancellation Rate'] != 1]   # strange edge case. one would think that it should be present

    df['Cancellation Rate'] = df['Cancellation Rate'].round(2)

    return df
