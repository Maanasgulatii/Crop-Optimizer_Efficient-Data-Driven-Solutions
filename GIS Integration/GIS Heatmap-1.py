import pandas as pd
import folium
from folium.plugins import HeatMap
import random

# Load your dataset
df = pd.read_csv('finaldataset.csv')

# Sample mapping of crops to rough latitude and longitude regions (this should be more accurate)
crop_regions = {
    'rice': [28.7041, 77.1025],     # Coordinates for Delhi
    'maize': [26.8467, 80.9462],    # Coordinates for Lucknow
    'apple': [32.2190, 76.3234],    # Coordinates for Himachal Pradesh
    'banana': [21.1458, 79.0882],   # Coordinates for Nagpur
    'coffee': [12.9716, 77.5946],   # Coordinates for Bangalore
    # Add more crops with approximate locations
}

# Add latitude and longitude columns to your dataset based on the 'label'
df['latitude'] = df['label'].apply(lambda x: crop_regions.get(x, [0, 0])[0] + random.uniform(-0.5, 0.5))
df['longitude'] = df['label'].apply(lambda x: crop_regions.get(x, [0, 0])[1] + random.uniform(-0.5, 0.5))

# Function to plot the heatmap for a specific crop
def plot_crop_heatmap(crop, df):
    # Filter the data for the given crop
    crop_data = df[df['label'] == crop]
    
    # Create a list of coordinates for the heatmap
    heat_data = [[row['latitude'], row['longitude']] for _, row in crop_data.iterrows()]
    
    # Add heatmap layer for the crop
    HeatMap(heat_data).add_to(base_map)

# Create a base map
base_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India

# List of all crops (labels)
crops = df['label'].unique()

# Iterate through the crops and plot each heatmap
for crop in crops:
    plot_crop_heatmap(crop, df)

# Display the final map
base_map.save("crop_heatmap.html")

# To display within Jupyter
base_map
