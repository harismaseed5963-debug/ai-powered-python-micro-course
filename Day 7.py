# Learning Python - Day 7
# Topic:
        # Strings Methods In Python
        # What are Strings Method In Python?
        # Why Strings Method In Python?

# # Practical Exercise Of the 7

# text = "   hello Python learners 2026    " 

# # Original Text
# print("Original:", text)

# # Remove Extra Spaces(strip)
# print("Remove Extra Spaces:", text.strip())

# # Change All Text To Capital Form(upper)
# print("The Capital Form Of All Text:", text.upper().strip())

# # Change All Text To Lower Form (lower)
# print("The Lower Form Of All Text:", text.lower().strip())

# # Change All Text To Proper Form (title)
# print("The Proper Form Of All Text:", text.title().strip())

# # Change the First Letter of the text to capital form(capitalize)
# print("Text After the changing of first letter into Capital Form of the text:", text.strip().capitalize())

# # Replace a part of the text(replace)
# print("Replace Python With Sql In The Text:", text.strip().replace("Python","Sql"))

## Break Text into words(split)
# split_text =text.strip().split()
# # print("Break Text Into Separate Words:",split_text)

# # Join All the Break Words Into Text(join)
# joined_text = "-".join(split_text)
# print("Joined all the break text:", joined_text)

# # Find The Index Of Specifc Letter(find)
# print("Find the position of 'P' in Text:", text.find('P'))

# # Find The Index but if not found then gives error
# print("Find the position of 'l' and if not found Then Gives :", text.index('l',7))

# # Check Whether the Text is Starts with Your Word(startswith)
# print("Check whether the text is start with hello after removing spaces:",text.strip().startswith('hello'))

# # Check Whether the Text is Ends with Your Word(endswith)
# print("Check whether the text is ends with hello after removing spaces:",text.strip().endswith('2026'))
