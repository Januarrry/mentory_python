weight = 4.8
# Ground shipping
if weight <= 2:
    print(weight * 1.5 + 20)
elif weight > 2 and weight <= 6:
    print(weight * 3 + 20)
elif weight > 6 and weight <= 10:
    print(weight * 4 + 20)
else:
    print(weight * 4.75 + 20)

flat_charge = 125
print(flat_charge)

# Dron
if weight <= 2:
    print(weight * 4.50)
elif weight > 2 and weight <= 6:
    print(weight * 9)
elif weight > 6 and weight <= 10:
    print(weight * 12)
else:
    print(weight * 14.25)
