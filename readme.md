Karan Chawla
Email: karancha@usc.edu
# User Behavior Analytics and Anomaly Detection Project

## Description of the Project
This project involves analyzing user activity data to detect anomalous behavior using machine learning techniques. The project consists of generating sample user activity data, detecting anomalies using Isolation Forest, performing predictive analysis using logistic regression, and visualizing the results using a Dash dashboard.

## Project Overview

1. Data Generation: Generate synthetic user activity data.
2. Anomaly Detection: Identify anomalous user behavior using Isolation Forest.
3. Predictive Analysis: Perform predictive analysis using logistic regression.
4. Visualization: Visualize user activities and anomalies using a Dash dashboard.

## Dependencies

Ensure you have Python installed. Install the necessary dependencies using the following command:
pip install pandas numpy scikit-learn dash plotly

## Steps to Run the Project

### Step 1: Data Generation - data_generation.py

Generate synthetic user activity data.
This script generates sample user activity data for a specified number of users over a given period. The data includes user ID, timestamp, and action performed (e.g., login, logout, file access). The generated data is saved to a CSV file named `user_activity.csv`.

Run the script:
python data_generation.py

### Step 2: Anomaly Detection - anomaly_detection.py

Identify anomalous user behavior using Isolation Forest.
This script loads the user activity data, performs feature engineering to extract relevant features (hour of activity, day of the week, action type), and groups the data by user ID. It then trains an Isolation Forest model to detect anomalies. The anomalous and normal user data are balanced and saved to a CSV file named `balanced_users.csv`.

Run the script:
python anomaly_detection.py

### Step 3: Predictive Analysis - predictive_analysis.py

Perform predictive analysis using logistic regression.
This script loads the balanced user data with anomaly scores, generates labels (0 for normal, 1 for anomalous), and splits the data into training and test sets. It trains a logistic regression model on the training data and evaluates the model's performance on the test data. The accuracy of the model is printed as the output.

Run the script:
python predictive_analysis.py

### Step 4: Visualization Dashboard - app.py

Visualize user activities and anomalies using a Dash dashboard.
This script creates a Dash web application to visualize user activities and detected anomalies. It loads the user activity data and the list of anomalous users. The dashboard includes two scatter plots: one showing all user activities and another highlighting the activities of anomalous users. The dashboard can be accessed via a web browser.

Run the script:
python app.py

### Dashboard Features

1. User Activities Visualization: A scatter plot showing the timestamp and user ID of various actions performed by users.
2. Anomalous User Activities Visualization: A scatter plot highlighting the activities of users detected as anomalous by the Isolation Forest model.

This project demonstrates the application of machine learning for anomaly detection and provides a visual representation of the results, making it easier to understand and analyze user behaviors.