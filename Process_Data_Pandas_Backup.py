import pandas as pd

# Load the dataset
# df = pd.read_csv('data/sales_data.csv')
df = pd.read_csv('sample_data.csv')

# Selecting Columns
sales = df['Revenue']
# selected_columns = df[['Sales', 'Region', 'Date']]
selected_columns = df[['Revenue', 'Country', 'LastPurchase']]

print("Selected Columns:")
print(selected_columns.head())

# Selecting Rows by Label with loc
first_row = df.loc[0]
print("\nFirst Row using loc:")
print(first_row)

# Selecting Rows by Position with iloc
first_five_rows = df.iloc[:5]
print("\nFirst Five Rows using iloc:")
print(first_five_rows)

# Filtering Data
high_sales = df[df['Revenue'] > 1000]
print("\nHigh Sales (>1000):")
print(high_sales)

# Adding a New Column
df['Sales_Tax'] = df['Revenue'] * 0.1
print("\nDataFrame with Sales_Tax:")
print(df.head())

# Dropping a Column
df.drop('Sales_Tax', axis=1, inplace=True)
print("\nDataFrame after Dropping Sales_Tax:")
print(df.head())

# Grouping and Aggregation
sales_by_country = df.groupby('Country')['Revenue'].sum()
print("\nTotal Sales by Country:")
print(sales_by_country)

# Handling Missing Values
# Fill missing 'Revenue' with the mean
df['Revenue'] = df['Revenue'].fillna(df['Revenue'].mean())
print("\nDataFrame after Filling Missing Revenue:")
print(df.head())

print("\nBefore dropping duplicates:")
print(df.shape)
# Remove duplicate rows
df.drop_duplicates(inplace=True)
print("\nDataFrame after Dropping Duplicates:")
print(df.shape)

## Conditional Filtering: Customers older than 40
customers_over_40 = df[df['Age'] > 40]
print(customers_over_40)

# Using query for complex conditions: Female customers from USA with Revenue > 500
filtered_customers = df.query("Gender == 'Female' and Country == 'USA' and Revenue > 500")
print(filtered_customers)

# Creating a Sales Category based on Quantity
def categorize_quantity(q):
    if q >= 7:
        return 'High'
    elif q >= 4:
        return 'Medium'
    else:
        return 'Low'

df['Quantity_Category'] = df['Quantity'].apply(categorize_quantity)
print(df[['Quantity', 'Quantity_Category']].head())

# Group by Gender and calculate total Revenue
revenue_by_gender = df.groupby('Gender')['Revenue'].sum()
print(revenue_by_gender)

# Group by Country and calculate average Revenue and Quantity
avg_revenue_quantity = df.groupby('Country').agg({'Revenue': 'mean', 'Quantity': 'mean'})
print(avg_revenue_quantity)

# Group by Product and Gender, then calculate total Revenue
revenue_product_gender = df.groupby(['Product', 'Gender'])['Revenue'].sum().unstack()
print(revenue_product_gender)

# Multiple Aggregations on Product
product_stats = df.groupby('Product').agg({
    'Revenue': ['sum', 'mean', 'max'],
    'Quantity': ['sum', 'mean']
})
print(product_stats)

# Count of Customers per Country
customer_count = df.groupby('Country')['CustomerID'].count()
print(customer_count)