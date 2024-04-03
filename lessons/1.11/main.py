# Перевороте строк или Polynomial
# Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке. (без использования встроенных функций)

# Input                   :       word = ‘abcde’
# Output                 :        word = ‘edcba’

word = "abcde"

for i in range(5, 1):
    print(i)
reversed_word = ""
for i in range(1, len(word) + 1):
    reversed_word = reversed_word + word[i * (-1)]
print(reversed_word)
