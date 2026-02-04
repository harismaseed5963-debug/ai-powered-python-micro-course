# Learning Python - Day 6
# 1. What is String in Python?
# 2. String Indexing 
# 3. String Slicing

# Practical Exercise Of The Day 6

# # How To Create A String
# string = "Haris" #('Haris', '''Haris''') String must be quoted in single, double or triple quotes
# print(string)  # Output: Haris

# String Indexing 
# Types:
#       Froward String Indexing 
#       Backward String Indexxing

# #Froward String Indexing:
# # It starts from 0 to n-1 (n is length of string)
# sample_string = "Python"
# print(sample_string[0])   # Output: P
# print(sample_string[1])  # Output: y
# print(sample_string[2])  # Output: t
# print(sample_string[3])  # Output: h    
# print(sample_string[4])  # Output: o
# print(sample_string[5])  # Output: n
# # print(sample_string[6])  # IndexError: string index out of range 

# # Backward String Indexing:
# # It starts from -1 to -n (n is length of string)   
# sample_data = "Haris"
# print(sample_data[-1]) # Output: s
# print(sample_data[-2]) # Output: i
# print(sample_data[-3]) # Output: r
# print(sample_data[-4]) # Output: a
# print(sample_data[-5]) # Output: H
# # print(sample_data[-6]) # IndexError: string index out of range

# # String Slicing
# # # It is used to extract a portion of string by using indexing
# # # Syntax: string_name[start_index:end_index] (end_index is excluded)
# sample_text = "Data Analysis"
# print(sample_text[0:4])   # Output: Data
# print(sample_text[5:13])  # Output: Analysis
# print(sample_text[0:13])  # Output: Data Analysis
# print(sample_text[5:])    # Output: Analysis
# print(sample_text[:4])    # Output: Data
# print(sample_text[-8:-1]) # Output: Analysi
# print(sample_text[-8:])   # Output: Analysis
# print(sample_text[:])     # Output: Data Analysis

# Assignment Of The Day

# #  Extracting year from product code
# product_code = "Laptop-Pro-2024"
# year = product_code[-4:]
# print("The Year Is:", year)

# #Extracting first name using slicing
# full_name = "Rohit Sharma"
# first_name = full_name[0:6]
# print("The First Name OF Rohit Sharma:", first_name)