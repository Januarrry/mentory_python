# craete an istagram photo rating app
# user inputs photo title
# user inputs photo likes
#
# 1. give feedback based on how many likes it has
#   less then 100 it is good
#   between 100 and 1000 excelent
#   between 1000 and 10000 you are getting famous
#   more then 10000 you are influencer
#
# 2. how many likes are needed till next feedback and what feedback it is for the photo title
# to calsulate likes for next step need

title = input("Your photo title: ")
likes = input("Type number of likes: ")
fb = int(likes)
ig = ""

if fb <= 100:
    ig = "Good"
elif fb >= 100 and fb <= 1000:
    ig = "Excelent"
elif fb >= 1000 and fb <= 10000:
    ig = "getting famous"
else:
    ig = "influencer"

print(ig)

if fb == 100:
    print("You not enough famos")
else:
    need_likes = fb * 100 + 1
    result = need_likes - 
    print("For", result + 1, "to be famos", result, "likes")
