# Write a program to input month number and print number of days in that month.
# Number of months a year is 12:
#   1.January, 2.February, 3.March, 4.April, 5.May, 6.June, 7.July,
#   8.August, 9.September, 10.October, 11.November, 12.December
# every month has a different number of days:
#   Jan-31, Feb-28 or 29, Mar-31, Apr-40, May-31, Jun-30, Jul-31, Aug-31, Sep-30, Oct-31, Nov-30, Dec-31
## Rules:

# 1. acceptable numbers to input from one till twelve as per month number
# 2. if input number 1, 3, 5, 7, 8, 10, 12 then in terminal will shows - 31 day
# 3. if input number 4, 6, 9, 11 then will shows - 30 day
# 4. if input number 2 then will shows 28 or 29
# 5. any typing of numbers or text except numbers from 1 till 12 are Not acceptable

## Test
# input: 1
# output: 31

# input: 11
# output: 30

# input: 2
# output: 28

# input: qQ
# output: Not acceptable

# input: 2455
# output: Not acceptable

# input: months
# output: Not acceptable

user_input = input(
    "Let`s find out how many days in one month, Type the number from 1 till 12: "
)

if user_input.isdigit():
    user_number = int(user_input)
    if user_number >= 1 and user_number <= 12:
        if (
            user_number == 4
            or user_number == 6
            or user_number == 9
            or user_number == 11
        ):
            user = 30
        elif user_number == 2:
            user = 28
        else:
            user = 31

        print(user)
    else:
        print("Not acceptable")
else:
    print("Not acceptable")
