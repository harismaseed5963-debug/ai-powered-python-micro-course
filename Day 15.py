# Learning Python - Day 15
# 1. What is Dictionay In Python?
# 2. Why Dictionaries Are Important For Data Analysts?

# Practical Exercise of The Day 15

# # Creating & Accessing Dictionaries
Employee = {"Name" : "Haris",
            "Age" : 18,
            "Role" : "Data Analyst"}

# print(Employee["Name"])
# print(Employee["Age"])


# # Accessing Values Using Keys

# Adding New Key_Value Pairs
Employee["Salary"] = 300000

# Updating Existing Values
# Employee["Age"] = 22

# # Removing Items
# Employee.pop("Salary")
# print(Employee)

# Employee.clear() # Output: Delete All The Data From Dictionay

# Looping Through Dictionary

# # Loop Keys
# for E in Employee:
#     print(E)

# # Loop Values
# for V in Employee.values():
#     print(V)

# # Loop Key_Value Pairs
# for k,v in Employee.items():
#     print(k, ":", v)

# # Nested Dictionaries

# student = {
#     "Stu01":{"Name": "Haris", "Class": "12th", "Group": "ICS"},
#     "Stu02":{"Name": "Kashif", "Class": "12th", "Group": "ICS"}
#      }
# # print(student)

# # Updating Nested Dictionary
# student["Stu01"]["Class"] = "13th"

# # Dictionary For Mapping Wrong Values => To Correct Values
# wrong_to_correct = {
#     'mumbai': "Mumbai",
#     'mombay' : "Mumbai",
#     'KolkaTta' : "Kolkata"
# }

# city = "mombay"
# print(wrong_to_correct[city])

# # Dictionary For Counting Frequency
# words = ['apple','banana','apple','mango']
# freq={}
# for w in words:
#  if w in freq:
#   freq[w] += 1
#  else:
#   freq[w] = 1
# print(freq)
# # Output:
# # {'apple': 2, 'banana': 2, 'mango': 1}

# # JSON- LIKE DICTIONARY(USED EVERYWHERE)
# product = {
#     "ID" : "P102",
#     "Name" : "Laptop",
#     "Ram" : "8GB",
#     "details" : {
#         "Brand" : "Dell",
#         "Color" : "Black"
#     }
# }
# print(product)