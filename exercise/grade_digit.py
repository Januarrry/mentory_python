# grade digit task

# inputs grade
# rules:
#  grade form 2 to 5 is passed
#  grade 1 is faile7d
#  all other is not found
#
#  1 is one, 2 is two, 3 is tree, 4 is four, 5 is five, else is invalid grade

# input:
#   2
# output:
#   Passed
#   You got two

# input:
#   1
# output:
#   Failed
#   You got one

# input:
#   5
# output:
#   Passed
#   You got five

# input:
#   3
# output:
#   Passed
#   You got tree

# input:
#   4
# output:
#   Passed
#   You got four

# input:
#   111
# output:
#   Not Found
#   You got invalid grade

# input:
#   -55
# output:
#   Not Found
#   You got invalid grade

# input:
#   6
# output:
#   Not Found
#   You got invalid grade

result = input("What is grade: ")
grade = int(result)

if grade >= 2 and grade <= 5:
    print("Passed")
elif grade == 1:
    print("Failed")
else:
    print("Not found")

word = ""
if grade == 5:
    word = "five"
elif grade == 4:
    word = "four"
elif grade == 3:
    word = "three"
elif grade == 2:
    word = "two"
elif grade == 1:
    word = "one"
else:
    word = "invalid grade"

print("You got " + word)


# -99 -1 0 1 2 3 4 5 6 7 8 99


# if True:
#     code1

# if True:
#     code2

# if False:
#     code3

# if True:
#     code4
# else:
#     code5

# if False:
#     code1
# elif True:
#     code2
# elif True:
#     code3


# if True:
#     code1
#     code1
#     code1
#     code1
#     code1
#     code1
#     code1
#     code1
# elif False:
#     code2
# elif True:
#     code3
# else:
#     code
