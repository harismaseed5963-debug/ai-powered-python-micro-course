# # Learning Python - Day 17
# #  1. What is .range() function in Python?
# #  2. Why .range() + Loops are important for data analysis?

# # Practical Examples of the Day 17

# # Print 1 To 5 Using range()
# for i in range(1, 6):
#     print(i)
# # Output: 1 2 3 4 5

# # Print Even Numbers Between 0 To 10
# for i in range(0, 11, 2):
#     print(i)
# # Output: 0 2 4 6 8 10

# # Print Countdown From 10 To 1
# for i in range(10, 0, -1):
#     print(i)
# # Output: 10 9 8 7 6 5 4 3 2 1

# # Print Loop through a List Using indexes
# my_list = ['a', 'b', 'c', 'd', 'e']
# for i in range(len(my_list)):
#     print(f"Index {i}: {my_list[i]}")
# # Output:
# # Index 0: a, Index 1: b, Index 2: c, Index 3: d, Index 4: e

# # Print Emp Id From 1 to 5
# for emp_id in range(1, 6):
#     print(f"Employee ID: {emp_id}")
# # Output: Employee ID: 1, Employee ID: 2, Employee ID: 3, Employee ID: 4, Employee ID: 5

# # Create year List
# years = []
# for i in range(2000, 2023):
#     years.append(i)
#     print(i)
# # Output: 2000, 2001, ..., 2022

# # Clean Cities Using range()
# cities = [' New York ', ' Los Angeles ', ' Chicago ', ' Houston ']
# cleaned_cities = []
# for i in range(len(cities)):
#     cleaned_cities.append(cities[i].strip())
# print(cleaned_cities)
# # Output: ['New York', 'Los Angeles', 'Chicago', 'Houston']

