import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Read Titanic passenger data from CSV file
file_path = "train.csv"
titanic_data = pd.read_csv(file_path)


# Create a bar chart with Seaborn
plt.figure(figsize=(8, 6))
sns.countplot(x="Sex", data=titanic_data)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Passenger Count by Gender")
plt.show()