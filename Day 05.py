# # Learning Python - Day 5
# # 1. Input Function In Python
# # 2. Why Input Function is Important?
# # 3. Problem with input that it stores data in string format
# # 4. Type Casting In Python

# # Practical Exercise Of The Day 5

# # Using input function to get user data
# user_name = input("Enter your name: ")  # Input as string
# user_age = input("Enter your age: ")    # Input as string
# print("Hello,", user_name)               # Output: Hello, <user_name>
# print("You are", user_age, "years old")  # Output: You are <

# # Solve the problem of input storing data in string format
# # by using type casting to convert age to integer

# # Change string age to integer
# user_age_int = int(user_age)             # Type casting to integer
# next_year_age = user_age_int + 1         # Calculate age for next year
# print("Next year, you will be", next_year_age, "years old")  # Output: Next year, you will be <next_year_age> years old

# # Change string age to float
# user_age_float = float(user_age)         # Type casting to float
# half_age = user_age_float / 2            # Calculate half age
# print("Half of your age is", half_age)    # Output: Half of your age is <half_age>

# # Total Sales Calculation:
# product = input("Product Name:")
# quantity = int(input("Enter Quantity Sold:"))
# price_per_unit = float(input("Enter Price Per Unit:"))

# total_sales = quantity*price_per_unit

# print("Product Name:", product)
# print("Total Sales Amount :", total_sales)

# # Assignment Of The Day

# # Salary Slip Calculator
# emp_name = input("Enter Your Name:")
# basic_salary = int(input("Enter Basic Salary:"))
# bonus = int(input("Enter Bonus Amount:"))
# tax_percentage = int(input("Enter Tax Percentage:"))

# Gross_Salary = basic_salary+bonus
# Tax_Amount = (Gross_Salary * tax_percentage)/100
# Net_Salary = Gross_Salary-Tax_Amount

# print("**** User Salary Slip **** ")
# print("Name:", emp_name)
# print("Gross Salary:", Gross_Salary)
# print("Tax Amount:", Tax_Amount)
# print("Net Salary:", Net_Salary)
