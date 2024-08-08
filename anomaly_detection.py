import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

# Load user activity data
df = pd.read_csv('user_activity.csv', parse_dates=['timestamp'])

# Feature engineering
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['action_code'] = df['action'].astype('category').cat.codes

# Group by user and aggregate features
user_features = df.groupby('user_id').agg({
    'hour': ['mean', 'std'],
    'day_of_week': ['mean', 'std'],
    'action_code': ['mean', 'std']
}).reset_index()
user_features.columns = ['user_id', 'hour_mean', 'hour_std', 'day_mean', 'day_std', 'action_mean', 'action_std']

# Train Isolation Forest model
contamination_level = 0.05
model = IsolationForest(contamination=contamination_level)
user_features['anomaly_score'] = model.fit_predict(user_features.drop('user_id', axis=1))

# Identify normal and anomalous users
anomalous_users = user_features[user_features['anomaly_score'] == -1]
normal_users = user_features[user_features['anomaly_score'] == 1]

# Manually balance the dataset if necessary
num_anomalous = len(anomalous_users)
num_normal = len(normal_users)

if num_anomalous == 0 or num_normal == 0:
    raise ValueError("No anomalous or normal users detected. Please adjust the contamination level.")

# Ensure balanced dataset
if num_anomalous > num_normal:
    anomalous_users = anomalous_users.sample(num_normal, random_state=42)
else:
    normal_users = normal_users.sample(num_anomalous, random_state=42)

balanced_users = pd.concat([anomalous_users, normal_users])
balanced_users.to_csv('balanced_users.csv', index=False)
anomalous_users.to_csv('anomalous_users.csv', index=False)  

print("Final Class Distribution:", balanced_users['anomaly_score'].value_counts())
