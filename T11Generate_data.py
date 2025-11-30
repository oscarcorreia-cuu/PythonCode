import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker for generating random names and dates
fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of samples
num_samples = 1000

# Generate CustomerID
customer_ids = np.arange(1, num_samples + 1)

# Generate Names
names = [fake.name() for _ in range(num_samples)]

# Generate Ages between 18 and 70
ages = np.random.randint(18, 71, size=num_samples)

# Generate Gender
genders = np.random.choice(['Male', 'Female', 'Other'], size=num_samples, p=[0.48, 0.48, 0.04])

# Generate Countries
countries = np.random.choice(['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'Brazil'], size=num_samples)

# Generate SignupDate between Jan 1, 2015 and Dec 31, 2023
signup_dates = [fake.date_between(start_date='-9y', end_date='today') for _ in range(num_samples)]

# Generate LastPurchase dates after SignupDate up to today
last_purchases = [fake.date_between(start_date=signup, end_date='today') for signup in signup_dates]

# Generate Product categories
products = np.random.choice(['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports', 'Beauty'], size=num_samples)

# Generate Quantity between 1 and 10
quantities = np.random.randint(1, 11, size=num_samples)

# Generate Price based on Product category
price_mapping = {
    'Electronics': np.random.uniform(100, 1000, size=num_samples),
    'Clothing': np.random.uniform(10, 200, size=num_samples),
    'Home & Kitchen': np.random.uniform(20, 500, size=num_samples),
    'Books': np.random.uniform(5, 100, size=num_samples),
    'Sports': np.random.uniform(15, 300, size=num_samples),
    'Beauty': np.random.uniform(5, 150, size=num_samples)
}
prices = [price_mapping[product][i] for i, product in enumerate(products)]

# Calculate Revenue
revenues = [round(q * p, 2) for q, p in zip(quantities, prices)]

# Generate Feedback scores with some missing values
feedbacks = np.random.choice([1, 2, 3, 4, 5, np.nan], size=num_samples, p=[0.1, 0.1, 0.2, 0.3, 0.2, 0.1])

# Create the DataFrame
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Name': names,
    'Age': ages,
    'Gender': genders,
    'Country': countries,
    'SignupDate': signup_dates,
    'LastPurchase': last_purchases,
    'Product': products,
    'Quantity': quantities,
    'Price': np.round(prices, 2),
    'Revenue': revenues,
    'Feedback': feedbacks
})

# Introduce some missing values randomly in 'Age' and 'Country' for demonstration
for _ in range(20):
    idx = np.random.randint(0, num_samples)
    df.at[idx, 'Age'] = np.nan

for _ in range(15):
    idx = np.random.randint(0, num_samples)
    df.at[idx, 'Country'] = np.nan

# Display first 5 rows of the generated dataset
print(df.head())

# Save the dataset to a CSV file
df.to_csv('sample_data.csv', index=False)

print("\nSample dataset 'sample_data.csv' with 1000 rows has been generated successfully.")
