# # Learning Python - Day 16
# # 1. What is a Set in Python?
# # Why Sets are important for data analysis?

# # Practical Examples of the Day 16

# # Creating a Set
# my_set = {1, 2, 3, 4, 5}
# print("Initial Set:", my_set)

# # Adding items to a Set
# my_set.add(6)
# print("Set after adding 6:", my_set)

# # Removing items from a Set
# my_set.discard(3)
# print("Set after removing 3:", my_set)

# # Set Operations:
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# # Union
# union_set = set_a.union(set_b)
# print("Union of set_a and set_b:", union_set)
# # Intersection 
# intersection_set = set_a.intersection(set_b)
# print("Intersection of set_a and set_b:", intersection_set)
# # Difference
# difference_set = set_a.difference(set_b)
# print("Difference of set_a and set_b:", difference_set)
# # Symmetric Difference
# symmetric_difference_set = set_a.symmetric_difference(set_b)
# print("Symmetric Difference of set_a and set_b:", symmetric_difference_set)

# # Remove Duplicates
# list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
# unique_list = list(set(list_with_duplicates))

# # Missing Values 
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# missing_values = a - b
# print("Missing values between set a and b:", missing_values)

# # Common Values
# common_values = a & b
# print("Common values between set a and b:", common_values)
