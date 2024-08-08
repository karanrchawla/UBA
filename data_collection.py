import pandas as pd
import numpy as np
import datetime

# Generate sample user activity data
np.random.seed(42)
num_users = 100
num_days = 30
user_ids = np.arange(1, num_users + 1)
date_range = pd.date_range(end=datetime.datetime.today(), periods=num_days).to_pydatetime().tolist()

data = []

for user_id in user_ids:
    for date in date_range:
        activity_count = np.random.poisson(lam=10)
        for _ in range(activity_count):
            timestamp = date + datetime.timedelta(minutes=np.random.randint(0, 1440))
            action = np.random.choice(['login', 'logout', 'file_access', 'email_sent', 'data_upload'], p=[0.3, 0.2, 0.3, 0.1, 0.1])
            data.append([user_id, timestamp, action])

df = pd.DataFrame(data, columns=['user_id', 'timestamp', 'action'])
df.to_csv('user_activity.csv', index=False)
print(df.head())
