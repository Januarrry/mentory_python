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
if grade == 4:
    word = "four"
if grade == 3:
    word = "three"
if grade == 2:
    word = "two"
if grade == 1:
    word = "one"
print("You got " + word)

# -99 -1 0 1 2 3 4 5 6 7 8 99
