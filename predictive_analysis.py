import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load user features and anomaly scores
user_features = pd.read_csv('balanced_users.csv')

# Generate labels (0 for normal, 1 for anomalous)
user_features['label'] = (user_features['anomaly_score'] == -1).astype(int)

# Split data into training and test sets
X = user_features.drop(['user_id', 'anomaly_score', 'label'], axis=1)
y = user_features['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
