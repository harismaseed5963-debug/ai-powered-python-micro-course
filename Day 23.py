# Learning Python - Day 23
# 1. Numpy Library In Python.
# 2. Who Created Numpy?
# 3. Why was Numpy Created?
# 4. Numpy Vs Python Lists
# 5. Why Data Analyst Must Learn Numpy First
# 6. Installing Numpy.

# Practical Exercise Of The Day 23

# # Installing And Importing Numpy
# # Installation: pip install numpy
import numpy as np
# arr = np.array([10,30,40,60])
# print(arr)

# # Create Array
# arr2 = np.array([35,32,65])
# print(arr2)

# # Create Array With Range
# arr3 = np.arange(1,11)
# print(arr3)

# # Array With Fixed Values
# zeros = np.zeros(5)
# ones = np.ones(5)

# # Random Array(Very Useful)
# rand = np.random.randint([10,15,20])
# print(rand)

# # Array Indexing
# indexing = np.array(arr)
# print(arr[1])
# print(arr[2])

# # Array Slicing
# slicing = np.array(arr)
# print(arr[0:2])
# print(arr[-3:])

# # Vectorized Operations
# # Addition
# arr = np.array([10,20])
# print(arr+10)

# # Multiplication
# print(arr*2)

# # Square Of All Items
# print(arr**3)

# # Array Functions (Data Cleaning + Data Analyses)
# # Sum,Mean,Max
# arr = np.array([10,20,30,40])
# print("Sum:", np.sum(arr))
# print("Average/Mean:", np.mean(arr))
# print("Maximum Value:", np.max(arr))

# # # Standard Deviation
# # print("Standard Deviation", arr.std())
# arr= np.arange(1,10)
# print(arr.reshape(3,3))

# Real Life Examples Of Numpy Arrays

# # Example 1: Remove Negative Values
# data = np.array([-10,20,30,-40,50,-60])
# clean = data[data >= 0]
# print(clean)

# # Example 2: Replace Missing Values
# missing_values = np.array([10,20,-1,40,-1,54,-1])
# missing_values[missing_values==-1] = [missing_values != -1].mean()

# # Example 3: Filtered Values Greater Than 20
# arr = np.array([43,21,28,13,65])
# filtered = arr[arr > 20]
# print(filtered)

# Example 4: Multiply all prices by prices(vectorized Calculation
qty = np.array([1,2,1,3])
price = np.array([100,200,300,400])
total = qty * price
print(total)
