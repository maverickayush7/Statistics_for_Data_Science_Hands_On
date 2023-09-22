import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Read Titanic passenger data from CSV file
file_path = "train.csv"
titanic_data = pd.read_csv(file_path)

# Calculate the correlation matrix
correlation_matrix = titanic_data.corr()

# Create a heat map with Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heat Map")
plt.show()