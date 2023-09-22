import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Read Titanic passenger data from CSV file
file_path = "train.csv"
titanic_data = pd.read_csv(file_path)

# Create a box plot with Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(x="Pclass", y="Age", data=titanic_data)
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.title("Age Distribution by Passenger Class")
plt.show()