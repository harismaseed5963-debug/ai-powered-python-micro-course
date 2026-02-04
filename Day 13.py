# Learning Python - Day 13
# 1. What Is Lists In Python?
# 2. Why Lists Are Important for Data Analyst?

# Practical Exercise Of The Day 13

# # Creating List
# fruits = ["Mango","Banana","Orange"]
# print(fruits)

# numbers = [23,24,53,54,32]
# print(numbers)

# Accessing Lists
cities = ["Lahore", "Karachi", "Peeshwar"]
# print(cities[0]) # Lahore
# print(cities[1]) # Karachi
# print(cities[-1]) # Peeshawar

# # Woking With Lists

# # Updatirng List Items
# cities[1] = "Islamabad"
# print(cities)

# # Adding items To A List
# cities.append("Pindi")
# print(cities)

# # Insert() --> Add at Position
# cities.insert(1,"Hydrabad")
# print(cities)

# # Removing Items From A List
# cities.remove("Karachi")
# cities.pop()
# cities.pop(2)
# print(cities)

# # List Slicing
# nums = [10,20,30,40]
# print(nums[1:4]) #[20,30,40]
# print(nums[:3]) # Print First 3 Numbers
# print(nums[-3:]) # Print Last 3 Numbers

# # List Looping
# for items in cities:
#      print(cities)

# # Checking Membership
# print("Karachi" in cities)
# print("Lahore" in cities)

# # Data Cleaning With Lists
# raw = ["  islamabad","PEShawar   ", "laHOre"]
# cleaned = []
# for c in raw:
#      cleaned.append(c.strip().title())

# print(cleaned)

# # Spelling Correction In Lists
# wrong = ["Mombai", "Kolkatta", "Bengluru"]
# correct = []
# for city in wrong:
#  city = city.replace("Mombai", "Mumbai") \
#  .replace("Kolkatta", "Kolkata") \
#  .replace("Bengluru", "Bengaluru")
#  correct.append(city)
# print(correct)

# # Calculate Total
# prices = [45,765,34,345,564]
# total = sum(prices)
# print("Total Price:",total)