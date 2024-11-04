import pandas as pd
import plotly.express as px

# Load your dataset
data = pd.read_csv('finaldataset.csv')

# Check for missing values and fill them if necessary
if data.isnull().sum().any():
    print("Missing values found in the dataset. Filling missing values with mean.")
    data.fillna(data.mean(), inplace=True)  # Fill missing values with mean

# Create a bar graph showing average rainfall by label
bar_data = data.groupby('label')['rainfall'].mean().reset_index()

# Create the bar graph
try:
    fig_bar = px.bar(bar_data, x='label', y='rainfall', 
                     title='Average Rainfall by Crop Type',
                     labels={'label': 'Crop Type', 'rainfall': 'Average Rainfall (mm)'},
                     color='rainfall')
    fig_bar.show()
except Exception as e:
    print("Error in creating bar graph:", str(e))

# Create a pie chart showing the distribution of crops
pie_data = data['label'].value_counts().reset_index()
pie_data.columns = ['label', 'count']

# Create the pie chart
try:
    fig_pie = px.pie(pie_data, names='label', values='count', 
                     title='Distribution of Crop Types',
                     color='label', 
                     color_discrete_sequence=px.colors.qualitative.Set3)
    fig_pie.show()
except Exception as e:
    print("Error in creating pie chart:", str(e))
