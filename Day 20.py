# Learning Python - Day 20
# 1.File Handling Through Python

# # Reading Full File
# with open("City.txt","r") as f:
#     print(f.read())

# # Reading Line By Line
# with open("City.txt","r") as f:
#     for line in f:
#         print(line.strip().title())


# # Writing(Overwright)
# with open("Notes.txt","w") as f:
#     f.write("Hi There!\n")
#     f.write("My Name Is Haris Ur Rehman\n")
#     f.write("I am a Data Anlayst Turning Raw Data Into Meaningfull Insights\n")

# # Apending
# with open("Notes.txt","a") as f:
#     f.write("I Use Tools Like Excel,PowerBi,Sql & Python")

# Cleaning Data In File 
# cleaned = []
# with open("City.txt","r") as f:
#     for line in f:
#         cleaned.append(line.strip().title())
# with open("Cleaned_Cith.txt","w") as f:
#     for city in cleaned:
#         f.write(city + "\n")

# # Counting Lines
# count = []
# with open("City.txt","r") as f:
#     for _ in f:
#         count += 1
#         print("Total Rows =",count)


