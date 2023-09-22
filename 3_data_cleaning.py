import pandas as pd
import numpy as np

# Generate synthetic sales data with missing values
np.random.seed(0)
data = {
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="M"),
    "Sales": np.random.choice([None, 1000, 2000, 3000, 4000], size=10),
}
sales_data = pd.DataFrame(data)

# Display the original dataset
print("Original Data:")
print(sales_data)

# Technique 1: Drop the Feature
sales_data_dropped_feature = sales_data.drop(columns=["Sales"])

# Technique 2: Drop the Observation
sales_data_dropped_observation = sales_data.dropna()

# Technique 3: Impute the Missing Values (using mean)
mean_sales = sales_data["Sales"].mean()
sales_data_imputed_mean = sales_data.copy()
sales_data_imputed_mean["Sales"].fillna(mean_sales, inplace=True)

# Display results
print("\nDropped Feature:")
print(sales_data_dropped_feature)

print("\nDropped Observation:")
print(sales_data_dropped_observation)

print("\nImputed Data (Mean):")
print(sales_data_imputed_mean)