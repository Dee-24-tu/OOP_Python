# Lab 5 - Strings
# Conceptual Practice

# No.1 Write a Python program to print each character of a string on a single line.
my_string = input("Enter a string: ")
for char in my_string:
    print(char)

# 2. Write a Python program that will calculate the length of a string
# (We already have a function len that does that, but we want to implement our own)

# my_string = input("Enter a string: ")
# print(len(my_string))


# 3. Given the string "Monty Python":
#   Write an expression to print the first character.
second_string = "Monty Python"
for char in second_string:
    print(second_string[0])
    break

#   Write an expression to print the last character.
#       (c) Write an expression including len to print the last character.
third_string = "Monty Python"
for char in third_string:
    print(third_string[len(third_string)-1])
    break


#       (d) Write an expression that prints "Monty".
#fourth_string = "Monty Python"
#for char in fourth_string:



# 4. Write a Python program that reads a string and prints a string that is made up of the first two characters and the last two characters. If the string has a length less than 4 the program prints a message on the screen.
#
# For example: “hello there” will result in “here”
#
# 5. Given a variable S containing a string of odd length:
# (a) Write an expression to print the middle character.
# (b) Write an expression to print the string up to but not including the middle character
# (i.e., the first half of the string).
# (c) Write an expression to print the string from the middle character to the end (not
# including the middle character).
#
# 6. Five string methods manipulate case: capitalize , title , swapcase , upper ,
# and lower . Consider the strings: s1 = "concord" , s2 = "souix city" , s3 =
# "HONOLULU" , and s4 = "TopHat".
# Describe what capitalize does.
# Describe what swapcase does.
# Describe what upper does.
# Describe what lower does.
# Describe what title does.