# Learning Python - Day 24
# 1. What Is Pandas?
# 2. Who Created Pandas?
# 3. Why Was Pandas Created?
# 4. Why Pandas Is Essential For Data Analysts?

#  Practical Work Of The Day 24
# import pandas as pd

# Load Csv Files 
# df = pd.read_csv(r"C:\Users\ij\Downloads\Players_dataset (1).csv")

# Print All Data Existing In Dataframe(Csv File)
# print(df)

# # Print The Top Rows Using .head() Function
# print(df.head())

# # Print The Bottom Rows Using .tail() Function
# print(df.tail())

# # Check The Shape Of The File
# print(df.shape)

#  Check The Number Of Coloumns In The File
# print(df.columns)

# # Check The Complete Information Of The File
# print(df.info())

# Describe The Data With (.describe) Function
# print(df.describe())

# # Clean Column Name
# df["name"]=df["name"].str.strip().str.title()
# print(df[["name","id"]])

# # Print Duplicates In your File
# print("Duplicate Values)",df.duplicated().sum())
# df = df.drop_duplicates()
# print(df)

# # Filter Data
# Pakistan = df[df["team"]=="Pakistan"]
# print(Pakistan)

# Pat_Cummins = df[df["name"]=="Pat Cummins"]
# print(Pat_Cummins)

# # Experienced And Un_Experienced Players
# exp_players = df[df["matches_played"] > 50]
# print("Experienced Players\n",exp_players)

# unexp_players = df[df["matches_played"] < 50]
# print("Un_Experienced Players",unexp_players)


# # Sort Data(By Matches Played)
# df_sorted = df.sort_values("matches_played", ascending=False)
# print(df_sorted.head)

# Group By With Pandas

# # Count Total Numbers Of Players From Each Team
# team_players = df.groupby(["team"])["name"].count()
# print(team_players)

# # Average Matches Played By Each Team Players
# ave_matches = df.groupby(["team"])["matches_played"].mean()
# print(ave_matches)

# # # Export Cleaned Data
# df.to_csv("Cleaned_Data.csv", index=False)