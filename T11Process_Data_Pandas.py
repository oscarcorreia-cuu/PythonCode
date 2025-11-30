import pandas as pd

# Load the dataset
# df = pd.read_csv('data/sales_data.csv')
df = pd.read_csv('sample_data.csv')
df = df[:-1]

# Selecting Columns
sales = df['Revenue']
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
# To check
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

# Sort DataFrame by Revenue in descending order
sorted_revenue = df.sort_values(by='Revenue', ascending=False)
print(sorted_revenue[['CustomerID', 'Revenue']].head())

# Sort by multiple columns: Country ascending, then Revenue descending
sorted_multi = df.sort_values(by=['Country', 'Revenue'], ascending=[True, False])
print(sorted_multi[['Country', 'Revenue']].head())

# Sort by Age in ascending order
sorted_age = df.sort_values(by='Age', ascending =False)
print(sorted_age[['CustomerID', 'Age']].head())

# Sorting by index
sorted_index = df.sort_index(ascending=False)
print(sorted_index.head())

# Get the unique list of countries
unique_countries = df['Country'].unique()

print("Unique Countries:")
print(unique_countries)

# Load the countries dataset
df_countries = pd.read_csv('countries.csv')

print("\nCountries Data:")
print(df_countries.head())

# Merge the sales data with countries data on 'Country' using a left join
df_merged = pd.merge(df, df_countries, on='Country', how='left')

# Display the first few rows of the merged dataset
print("\nMerged Data:")
print(df_merged.head())

print(df_merged['CustomerID'].head())

# To print two fields you need to remember the extra bracket
print(df_merged[['CustomerID','Continent']].head())

# Step 7: Calculate Revenue per Continent
revenue_per_continent = df_merged.groupby('Continent')['Revenue'].sum().reset_index()
revenue_per_continent = revenue_per_continent.sort_values(by='Revenue', ascending=False)
print("\nRevenue per Continent:")
print(revenue_per_continent)

# Load the inquiries data (new dataset with unique CustomerIDs)
df_inquiries = pd.read_csv('inquiries_data.csv')

# Perform a left join to find inquiries not in sales
inquiries_with_sales = pd.merge(
    df_inquiries,
    df[['CustomerID']],  # Only CustomerID column needed from sales data
    on='CustomerID',
    how='left',
    indicator=True  # Adds a column "_merge" to indicate presence in either or both datasets
)

# Filter for inquiries not in sales (where '_merge' == 'left_only')
inquiries_not_in_sales = inquiries_with_sales[inquiries_with_sales['_merge'] == 'left_only']

# Count the number of such inquiries
count_inquiries_not_in_sales = inquiries_not_in_sales.shape[0]

print("Count of inquiries not in sales:", count_inquiries_not_in_sales)