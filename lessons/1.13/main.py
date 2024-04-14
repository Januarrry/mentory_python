# List sorting problem:
# Write a program that accepts a list with numbers and the output should be a sorted array (without using built-in functions).
# Input: lst = [1,5,4,8,101,67]
# Output: lst = [1,4,5,8,67,101]

list = [1, 5, 4, 8, 101, 67]
for i in range(len(list)):
    for q in range(i + 1, len(list)):
        if list[i] > list[q]:
            list[i], list[q] = list[q], list[i]
            print(list)
