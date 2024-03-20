grade_word = input("Type your grade: ")
not_found = False

number = ""
if grade_word == "five":
    number = 5
elif grade_word == "four":
    number = 4
elif grade_word == "three":
    number = 3
elif grade_word == "two":
    number = 2
elif grade_word == "one":
    number = 1
else:
    not_found = True

if not_found == True:
    print("Not valid ")
else:
    print("Your grade is", grade_word)

    if number >= 2 and number <= 5:
        print("Passed")
    else:
        print("Failed")
