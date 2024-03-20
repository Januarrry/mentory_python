# to get driving license need to pass exams here input your score of exams
# you may pass exams 4 times but it depends how many score you get when failed:
# score from 0 to 10 not not allowed to take next exams need relearn theory
# score from 11 to 22 you may have one chance to try again
# score from 23 to 32 you may try next week
# score from 33 to 40 you may try to pass it next day
# score from 41 to 45 Congrats with new drivers license
# score less than 0 and more than 46 not found
# if result is digits score can be execute if not digit its not execute


result = input("Here type your score: ")


if result.isdigit():
    score = int(result)

    if score >= 0 and score <= 10:
        s = "Not allowed to take next exams need relearn theory"
    elif score >= 11 and score <= 22:
        s = "You may have one chance to try again"
    elif score >= 23 and score <= 32:
        s = "You may try next week"
    elif score >= 33 and score <= 40:
        s = "You may try to pass it next day"
    elif score >= 41 and score <= 45:
        s = "Congrats with new drivers license"
    else:
        s = "Not found"
    print(s)

else:
    print("Type only digits")
