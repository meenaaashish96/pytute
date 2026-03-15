# Task3: 
# """
#   This is   a test.

# Python   is fun!  

#    Can you   solve it? 
# """

# Remove all extra spaces (more than 1) and leading/trailing spaces on each line.
# Remove empty lines.
# Replace all newline characters (\n) with a single space.
# Capitalize the first letter of each sentence (sentence ends with ., !, or ?).
# Ensure the final string has only single spaces between words.

# output : "This is a test. Python is fun! Can you solve it?"

strxyz = """
  This is   a test.

Python   is fun!  
          
   Can you   solve it? 
"""
splited = strxyz.splitlines()
#print(splited[1])
newstring = ''
for row in splited:
    if row != "":
        newstring += row

print(" ".join(newstring.split()))