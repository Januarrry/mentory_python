# create grade_points.py
#     should input digit points you got(1-100)
#     should print grade in digits:
#         00-50: 5
#         51-60: 6
#         61-70: 7
#         71-80: 8
#         81-90: 9
#         91-100: 10
#         else wrong points

#     should print how many points we need to next grade and the next grade
#     ex 87 - you need 4 points for 10

grade_points = input("You got points: ")

if not grade_points.isdigit():
    print("you must enter digit")
else:
    points = int(grade_points)

    level = -1
    if points >= 0 and points <= 50:
        level = 5
    elif points >= 51 and points <= 60:
        level = 6
    elif points >= 61 and points <= 70:
        level = 7
    elif points >= 71 and points <= 80:
        level = 8
    elif points >= 81 and points <= 90:
        level = 9
    elif points >= 91 and points <= 100:
        level = 10

    if level == -1:
        print("Wrong points")
    else:
        print("You have level", level)

        if level == 10:
            print("Congrats! You got heighes level")
        else:
            need_points = level * 10 + 1
            result = need_points - points
            print("For", level + 1, "level you need", result, "points")
