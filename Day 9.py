# Learning Python - Day 9
# 1. Nested If Funtion
# 2. Syntex of Nested If Function
# 3. Daily Life examples of Nested If Funtion
# 4. What are Multiple Conditions?
# 5. Multiple Conditions Daily Life Examples

# Practical Exercise Of The Day 9

# # Age And ID_Card Identifier
# age = int(input("Enter Your Age:"))
# id_card =(input("Do Your Have An ID_Card:(Yes/No)"))
# if age >=18:
#     if id_card == id_card.lower():
#         print("You Are Eligibal For Voting")
#     else:
#         print("You Have No ID_Card So You Are Not Eligibal")
# else:
#     print("You Are Under Age")


# # Go On A Picnic Prediction

# weekday = input("Enter The Weekday:")
# weather = input("Type Of Weather(Sunny/Rainy):")

# if weekday.title() == "Sunday":
#     if weather.title() == "Sunny":
#         print("Go For Picnic")
#     else:
#         print("Cancel The Picnic Due to Bad Whether")
# else:
#     print("Cancel the Picnic Because Today Is Not a Weekend")

# # Customer Discount Eligibility
# amount = int(input("Enter Customer Amount:"))
# is_member =input("Are You Memeber before with Us(True/False):")

# if amount >= 1000:
#     if is_member.title()=="True":
#         print("Congratulations,You Have Get The Discount")
#     else:
#         print("Sorry, You Have't Get The Discount Visit Next Time For Getting Discount")
# else:
#     print("Sorry, Your Amount Is Low Than Our DIscount Limit")

# # Driving Eligibility(Multiple Conditions)
# age = int(input("Enter Your Age:"))
# has_license = input("Do You Have Driving License(Yes/No):")
# if age >= 18 and has_license.lower() == "yes":
#     print("You Are Eligible To Drive")
# else:
#     print("You Are Not Eligible To Drive")
