import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Read Titanic passenger data from CSV file
file_path = "train.csv"
titanic_data = pd.read_csv(file_path)

# Sample monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12000, 15000, 18000, 14000, 16000, 19000, 22000, 24000, 21000, 23000, 26000, 28000]

# Good Visualization: Line Plot
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
