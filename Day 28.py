# # Learning Python - Day 28
# # 1. Practical Automation Using Ai

# # Pompt:
# """"
# Write a Python program that asks the user to
# paste the folder path containing multiple CSV
# files when the program runs. After pressing
# Enter, the program should automatically read
# all CSV files from that folder and combine
# them into one Excel workbook.
# Each CSV file should be placed in a separate
# sheet, and the sheet name must match the
# CSV file name. The program should then save
# the Excel workbook in the same folder where
# the CSV files are located, with the name
# “All_CSV_Converted_Into_Sheets.xlsx”.
# """
# # Output Code:
# import os
# import pandas as pd

# # Ask the user for the folder path containing the CSV files
# folder_path = input("Please paste the folder path containing the CSV files: ").strip()

# # Verify if the folder path is valid
# if not os.path.isdir(folder_path):
#     print("The provided folder path is not valid. Please try again.")
# else:
#     # Create a new Excel writer object
#     excel_file = os.path.join(folder_path, "All_CSV_Converted_Into_Sheets.xlsx")

#     # Create an Excel writer
#     with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
#         # Loop through each CSV file in the folder
#         for file_name in os.listdir(folder_path):
#             if file_name.endswith('.csv'):
#                 # Read the CSV file
#                 csv_file_path = os.path.join(folder_path, file_name)
#                 df = pd.read_csv(csv_file_path)
                
#                 # Clean the sheet name to remove invalid characters (like .)
#                 sheet_name = os.path.splitext(file_name)[0]
                
#                 # Write the DataFrame to the corresponding sheet
#                 df.to_excel(writer, sheet_name=sheet_name, index=False)
    
#     print(f"All CSV files have been converted into sheets and saved to {excel_file}")
