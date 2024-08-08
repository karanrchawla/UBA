import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('user_activity.csv', parse_dates=['timestamp'])
anomalous_users = pd.read_csv('anomalous_users.csv')

# Create Dash app
app = dash.Dash(__name__)

# Visualize user activities
fig = px.scatter(df, x='timestamp', y='user_id', color='action', title='User Activities')

# Visualize anomalies
anomalies = df[df['user_id'].isin(anomalous_users['user_id'])]
fig_anomalies = px.scatter(anomalies, x='timestamp', y='user_id', color='action', title='Anomalous User Activities')

app.layout = html.Div(children=[
    html.H1(children='User Behavior Analytics Dashboard'),
    dcc.Graph(
        id='user-activities',
        figure=fig
    ),
    dcc.Graph(
        id='anomalous-user-activities',
        figure=fig_anomalies
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
