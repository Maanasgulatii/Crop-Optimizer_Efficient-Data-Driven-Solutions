import plotly.express as px

fig = px.scatter(data, x='humidity', y='temperature', color='rainfall',
                 title='Interactive Scatter Plot of Temperature vs Humidity',
                 labels={'humidity': 'Humidity (%)', 'temperature': 'Temperature (°C)', 'rainfall': 'Rainfall (mm)'})
fig.show()
