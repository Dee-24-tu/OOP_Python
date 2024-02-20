#Lab 3: If-else, if-elif-else, repetition
#The objective is to practise the concepts of conditionals and repetitions in Python.
#Conceptual Practice
#No 1:
user = input("Enter a mark (between 0 and 100): ")
mark = 0
if mark <= 40:
    print("This is fail")

if mark >= 40:
    print("This is a pass")

#No 2:
user_first = int(input("Enter a number"))
user_second = int(input("Enter a number"))
if user_first > user_second:
    print("This is large.")
elif user_second < user_first:
    print("This is small.")
elif user_first == user_second:
    print("This is equal.")

# No 3:

# No 4:

# No 5:

# No 6:


# 06-02-2024 Tuesday
# No 7:
x = int(input("Enter a number"))

total = 0
for i in range(1, x + 1):
    total += 1

for i in range(1, x + 1):
    total = 0
    for addition in range(1, x + 1):
        total += addition

    # if total % addition == 0:

    print(total)

# Critical Thinking Tasks
# No. 5
for j in range(1,11):
    for i in range(1,11):
        print(1, "*", j, "=",i * j)

# No. 6