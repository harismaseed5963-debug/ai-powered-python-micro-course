# Learining Python - Day 26
# 1.What Does "Ai Enabled Python" Mean?
# 2.Why Analyst Must Learn Ai Enabled Python?
# 3.Where Ai Fits In Data Analysis Workflow?
# 4.What Ai Can Do?

# Practical Exercise Of The Day 26
# Prompt For Ai Enabled Python To Generate Code
"""I have a CSV file with employee data file name is day24_Employee_Data.csv
Columns: Employee_ID,Employee_Name,Department,City,Salary,Joining_Year
Generate Pandas code to:
1. Clean names and cities
2. Remove duplicates
3. Add Experience column"""

# # Generated Code:
# import pandas as pd

# # Load the CSV file
# df = pd.read_csv('day24_Employee_Data.csv')

# # 1. Clean names and cities (strip whitespaces, convert to title case)
# df['Employee_Name'] = df['Employee_Name'].str.strip().str.title()
# df['City'] = df['City'].str.strip().str.title()

# # 2. Remove duplicates
# df = df.drop_duplicates()

# # 3. Add Experience column (assuming current year is 2026 for simplicity)
# df['Experience'] = 2026 - df['Joining_Year']

# # Display the cleaned DataFrame
# print(df)

