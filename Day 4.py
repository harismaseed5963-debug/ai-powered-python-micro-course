# # Learning Python - Day 4
# # 1. Operators In Python
# # 2. Different Types Of Operators In Python
# # 3. Arithmetic, Assignment, Comparison, Logical, Identity, Membership & Bitwise 

# # Practical Exercise Of The Day 4

# # Arithmetic Operators
# a = 10
# b = 3   
# print("Addition:", a + b)            # Output: 13
# print("Subtraction:", a - b)         # Output: 7
# print("Multiplication:", a * b)      # Output: 30
# print("Division:", a / b)            # Output: 3.3333...
# print("Modulus:", a % b)             # Output: 1
# print("Exponentiation:", a ** b)     # Output: 1000

# # Assignment Operators
# c = 5
# c += 2  # c = c + 2
# print("c after += 2:", c)            # Output: 7
# c *= 3  # c = c * 3 
# print("c after *= 3:", c)            # Output: 21
# c -= 4  # c = c - 4
# print("c after -= 4:", c)            # Output: 17
# c /= 2  # c = c / 2
# print("c after /= 2:", c)            # Output: 8.5

# # Comparison Operators
# x = 10
# y = 20
# print("x == y:", x == y)              # Output: False
# print("x != y:", x != y)              # Output: True
# print("x > y:", x > y)                # Output: False
# print("x < y:", x < y)                # Output: True
# print("x >= y:", x >= y)              # Output: False
# print("x <= y:", x <= y)              # Output: True

# # Logical Operators
# p = True
# q = False
# print("p and q:", p and q)            # Output: False
# print("p or q:", p or q)              # Output: True
# print("not p:", not p)                 # Output: False

# # Identity Operators
# m = [1, 2, 3]
# n = m
# print("m is n:", m is n)              # Output: True
# o = [1, 2, 3]
# print("m is not o:", m is not o)      # Output: True

# # Membership Operators
# fruits = ["apple", "banana", "cherry"]
# print("banana in fruits:", "banana" in fruits)        # Output: True
# print("grape not in fruits:", "grape" not in fruits)  # Output: True

# # Bitwise Operators
# num1 = 5  # Binary: 0101
# num2 = 3  # Binary: 0011
# print("num1 & num2:", num1 & num2)    # Output: 1 (Binary: 0001)
# print("num1 | num2:", num1 | num2)    # Output: 7 (Binary: 0111)
# print("num1 ^ num2:", num1 ^ num2)    # Output: 6 (Binary: 0110)

# # Real Life Example Using Operators In Python
# price = 1000
# discount = 200
# final_price = price - discount
# print("Final Price Is :", final_price) # Output: Final Price Is : 800