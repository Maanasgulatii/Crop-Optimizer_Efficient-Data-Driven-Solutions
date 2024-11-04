import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('finaldataset.csv')

# Check for missing values and fill them if necessary
if data.isnull().sum().any():
    data.fillna(data.mean(), inplace=True)  # Fill missing values with mean

# Create a correlation matrix using only numeric columns
correlation_matrix = data.select_dtypes(include=[np.number]).corr()

# Plotting the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
