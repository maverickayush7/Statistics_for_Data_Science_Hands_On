import pandas as pd

# Read Titanic passenger data from CSV file
file_path = "train.csv"
titanic_data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the Titanic DataFrame:")
print(titanic_data.head())

# Display column names
print("\nColumn names:")
print(titanic_data.columns)

# Display number of rows and columns
print("\nNumber of rows and columns:")
print(titanic_data.shape)

# Summary statistics
print("\nSummary statistics:")
print(titanic_data.describe())

# Filter passengers with age greater than 60
senior_passengers = titanic_data[titanic_data['Age'] > 60]
print("\nPassengers with age greater than 60:")
print(senior_passengers)

# Sort passengers by fare in descending order
sorted_data = titanic_data.sort_values(by='Fare', ascending=False)
print("\nSorted data by fare:")
print(sorted_data.head())

# Group by passenger class and calculate averages
class_avg = titanic_data.groupby('Pclass').agg({'Age': 'mean', 'Fare': 'mean'})
print("\nAverage age and fare by passenger class:")
print(class_avg)

# Data visualization: Survival rate by passenger class
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=titanic_data, ci=None)
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Passenger Class')
plt.show()
