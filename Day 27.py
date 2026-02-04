# # Leearning Python - Day 27
# # 1.What is a Data Pipeline?
# # 2.Why Automation Matters For Data Analysts?
# # 3.Role Of Ai in Pandas Pipelines

# # Practical Exercise of the Day 27

# # Pipelline Automation using Pandas and AI Prompt:
# """""I have a raw sales CSV file with columns like:
# Order_ID,Order_Date,Customer_Name,City,State,Product_Category,
# Product_Name,Quantity,Unit_Price,Discount,Payment_Mode,Sales_
# Channel
# Create a Pandas automation pipeline to:
# 1. Clean customer names, city and state values
# 2. Remove duplicate orders
# 3. Convert numeric columns properly
# 4. Calculate Total_Sales = (Quantity * Unit_Price) - Discount
# 5. Categorize orders as High / Medium / Low value
# 6. Create summary reports:
#  - Total sales by City
#  - Total sales by Product_Category
# 7. Sort summaries in descending order
# 8. Export cleaned data and summaries to CSV files"""

# # Resulting Code:
# import pandas as pd

# # Load the raw sales CSV file
# df = pd.read_csv('raw_sales_data (1).csv')

# # 1. Clean customer names, city, and state values
# df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()
# df['City'] = df['City'].str.strip().str.title()
# df['State'] = df['State'].str.strip().str.title()

# # 2. Remove duplicate orders
# df = df.drop_duplicates(subset='Order_ID')

# # 3. Convert numeric columns properly
# df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
# df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')
# df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')

# # 4. Calculate Total_Sales = (Quantity * Unit_Price) - Discount
# df['Total_Sales'] = (df['Quantity'] * df['Unit_Price']) - df['Discount']

# # 5. Categorize orders as High / Medium / Low value based on Total_Sales
# def categorize_order(row):
#     if row['Total_Sales'] > 500:
#         return 'High'
#     elif row['Total_Sales'] > 100:
#         return 'Medium'
#     else:
#         return 'Low'

# df['Order_Value'] = df.apply(categorize_order, axis=1)

# # 6. Create summary reports

# # Total sales by City
# sales_by_city = df.groupby('City')['Total_Sales'].sum().sort_values(ascending=False)

# # Total sales by Product_Category
# sales_by_category = df.groupby('Product_Category')['Total_Sales'].sum().sort_values(ascending=False)

# # 7. Sort summaries in descending order
# sales_by_city_sorted = sales_by_city.sort_values(ascending=False)
# sales_by_category_sorted = sales_by_category.sort_values(ascending=False)

# # 8. Export cleaned data and summaries to CSV files
# df.to_csv('cleaned_sales_data.csv', index=False)
# sales_by_city_sorted.to_csv('sales_by_city.csv')
# sales_by_category_sorted.to_csv('sales_by_category.csv')

# print("Pipeline executed successfully, files exported!")
