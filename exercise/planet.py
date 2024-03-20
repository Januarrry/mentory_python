# calculate acceptable weight for space
# Input: weight in kg
# Output: calculated result
# rules:
# weight less that 0 zero and typing weight in text not valid, type only digits
# weight 100 one hundred and more than 100 not found,
# weight 0 zero or more than 0 zero and less than 45 fourty five not found,
# weight 45 forty five or more than 45 fourty five and 59 fifty nine or less than 59 fifty nine not enought weight,
# weight 60 sixty or more than 60 sixty and less than 80 eighty is acceptable,
# weight 81 eighty one or more than 81 eighty one and less than 90 ninety is normal weight,
# weight 90 ninty or more than 90 ninety and less than 99 one hundred overweight,

# input: -5
# output:
#   Not valid, type only digits

# input: 0
# output:
#   Not found

# input: kjhalkhlgh
# output:
#   Not valid, type only digits

# input: 40
# output:
#   Not found

# input: 45
# output:
#   Not enought weight

# input: 50
# output:
#   Not enought weight

# input: 60
# output:
#   Your weight is acceptable

# input: 70
# output:
#   Your weight is acceptable

# input: 90
# output:
#   Not acceptable
#   You have normal weight

# input: 100
# output:
#   Not found

user_input = input("Write kg weight: ")
is_user_input_a_digit = user_input.isdigit()
if user_input.isdigit():

    kg = int(user_input)
    print("Your weight is: " + str(kg))
    w = ""
    if kg >= 45 and kg <= 59:
        w = "Not enought weight"

    if kg >= 60 and kg <= 80:
        w = "Weight is acceptable "

    if kg >= 81 and kg <= 90:
        w = "You have normal weight"

    if kg >= 91 and kg <= 99:
        w = "You have overweight"
    else:
        w = "Not found"

    print(w)

else:
    print("Not valid, type only digits ")
