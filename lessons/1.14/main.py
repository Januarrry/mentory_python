# Palindrome checking problem:
# Write a program that asks the user for a word or phrase and determines whether it is:
# Input: word = ‘Abc-cbA’
# Output: True
# Input: word = ‘helloolleh’
# Output: True

# find a middle
# checking letter by letter
# imagine line starting from 0 checking position 1 with -1, 2 with -2, 3 with -3


word = "Abc- CbA"
middle = int(len(word) / 2)
palindrome = True
for left_index in range(middle):
    right_index = left_index * -1 - 1
    palindrome = palindrome and word[left_index] == word[right_index]

print(palindrome)
