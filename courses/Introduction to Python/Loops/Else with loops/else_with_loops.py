i = 0
while i < 5:
    print('it\'s less than 5')
    i += 1
else:
    print('and now it\'s 5')  # Print this message when the condition is no longer True

for i in range(1, 5):
    print(i)
    if i == 2:# Add a condition for interruption.
        break # Add a statement that will terminate the loop.
else:
    print("for loop is done")

print("Outside the for loop")
