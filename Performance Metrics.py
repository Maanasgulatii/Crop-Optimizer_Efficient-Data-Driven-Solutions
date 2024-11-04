import matplotlib.pyplot as plt
import numpy as np

# Dictionary containing performance metrics for each crop
rf_report_dict = {
    'apple': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'banana': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'blackgram': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'chickpea': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'coconut': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'coffee': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'cotton': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'grapes': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'jute': {'precision': 0.92, 'recall': 1.00, 'f1-score': 0.96},
    'kidneybeans': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'lentil': {'precision': 0.92, 'recall': 1.00, 'f1-score': 0.96},
    'maize': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'mango': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'mothbeans': {'precision': 1.00, 'recall': 0.96, 'f1-score': 0.98},
    'mungbean': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'muskmelon': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'orange': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'papaya': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'pigeonpeas': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'pomegranate': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00},
    'rice': {'precision': 1.00, 'recall': 0.89, 'f1-score': 0.94},
    'watermelon': {'precision': 1.00, 'recall': 1.00, 'f1-score': 1.00}
}

# Extracting metrics for plotting
crop_labels = list(rf_report_dict.keys())
precision = [rf_report_dict[label]['precision'] for label in crop_labels]
recall = [rf_report_dict[label]['recall'] for label in crop_labels]
f1_scores = [rf_report_dict[label]['f1-score'] for label in crop_labels]

# Set up the bar chart
x = np.arange(len(crop_labels))
width = 0.25  # Width of the bars

fig, ax = plt.subplots(figsize=(14, 8))
rects1 = ax.bar(x - width, precision, width, label='Precision')
rects2 = ax.bar(x, recall, width, label='Recall')
rects3 = ax.bar(x + width, f1_scores, width, label='F1 Score')

# Add labels, title, and customize x-axis tick labels
ax.set_xlabel('Crops', fontsize=14)
ax.set_ylabel('Scores', fontsize=14)
ax.set_title('Performance Metrics for Crop Recommendation Model', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(crop_labels, rotation=45, ha='right', fontsize=10)
ax.legend()

# Tight layout for better spacing
fig.tight_layout()

# Show the plot
plt.show()
