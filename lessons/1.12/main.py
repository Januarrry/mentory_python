# Problem about finding prime numbers:
# The program should use only basic operators and should not rely on built-in functions or libraries
# Input: n = 10
# Output: lst = [2, 3, 5, 7]

n = 9
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num1 = n / num[0]
# for i in range(10):
print(num1)
num2 = n / num[1]
print(num2)
# num3 = n / num[2]
# print(num3)
# num4 = n / num[3]
# print(num4)
if n % num[1] == 0:
    q = "not prime"
else:
    q = "prime"
print(q)
