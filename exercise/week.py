# Write a program to input day number(1-7) and
# print the corresponding day of week name(Monday, Tuesday, Wednesday)
## Rules
# input the number from 1 till 7 in terminal will show the name of day
# input accepted only numbers and only from 1 till 7, otherwise input invalid
# 1-Monday, 2-Tuesday, 3-Wednsday, 4-Thursday, 5-Friday, 6-Saturday, 7-Sunday
##Test
# input: 1
# output: Monday

# input: sdff
# output: invalid input

# input: 8
# output: invalid input

# days = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
# number = [1, 2, 3, 4, 5, 6, 7]

user_input = input("Type number of day: ")

if user_input.isdigit():
    day_number = int(user_input)
    if day_number == 1:
        day = "Monday"
    elif day_number == 2:
        day = "Tuesday"
    elif day_number == 3:
        day = "Wednsday"
    elif day_number == 4:
        day = "Thursday"
    elif day_number == 5:
        day = "Friday"
    elif day_number == 6:
        day = "Saturday"
    elif day_number == 7:
        day = "Sunday"
    else:
        day = "invalid input"
    print(day)
else:
    print("invalid input")
