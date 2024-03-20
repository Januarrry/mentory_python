## Description
# Write a program to input any alphabet and check whether it is vowel or consonant.
# input any letter to check which is vowel or consonant
# vowel letters a, e, i, o, u, and sometimes y
#
## Rules
# if user inputs vowel(a,e,i,o,u) then should display on the terminal vowel
# if user inputs consonat(other letter then a,e,i,o,u) then should display on the terminal consonant
# input "y" output: "sometimes vowel"
# if user inputs anything else other then 1 letter then should display on terminal invalid input

## Tests
# input: a
# output: vowel
#
# input: u
# output: vowel
#
# input: c
# output: consonant
#
# input: z
# output: consonant
#
# input: asdasda
# output: invalid input
#
# input: 2
# output: invalid input
#
# input:
# output: invalid input
#
# input: y
# output: sometimes vowel

user_input = input("Type letter: ")

if len(user_input) == 1 and user_input.isalpha():

    if (
        user_input == "a"
        or user_input == "e"
        or user_input == "i"
        or user_input == "o"
        or user_input == "u"
    ):
        letter = "vowel"
    elif user_input == "y":
        letter = "sometimes vowel"
    else:
        letter = "consonant"

    print(letter)

else:
    print("invalid input")
