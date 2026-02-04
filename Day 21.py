# Learning Python - Day 21
# 1. Reading Csv Files
# 2. Read As Dictionary

# Practical Exercise Of The Day 21

import csv

# Readiing CSV Files(Without Pandas)
with open("Players_dataset (1).csv","r") as f:
    reader = csv.reader(f)
    for row in f:
        print(row)

