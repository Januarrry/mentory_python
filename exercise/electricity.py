## Description
# Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units USD 0.50/unit
# For next 100 units USD 0.75/unit
# For next 100 units USD 1.20/unit
# For unit above 250 USD 1.50/unit
# An additional surcharge of 20% is added to the bill
# Rules:
# input electricity unit, output: electricity bill:
# For every calculation of electricity bill need add extracharge 20%
#   electricity bill = (electricity unit * price per unit) + 20%
# if input first 50 units so price per unit is 0.50, output: electricity bill = (input*0.50)+ 20%
# if input next 100 units then price is 0.75 per unit, output: electricity bill = ((input - 50)*0.75 + 50*0.5) + 20%
# if unit next 100 units then price is 1.20 per unit, output: electricity bill = ((input - 150)*1.2 + 50*0.5 + 100*0.75) + 20%
# if above 250 units then price is 1.50 per unit, output: electricity bill = ((input - 250)*1.5 + 50*0.5 + 100*0.75 + 100*1.2) + 20%
# Only positive numbers input are acceptable
##Test:
# input: 49
# output: 29.4
# calculation as per formula: (49*0.5)+0.2=29.4
#
# input: 95
# output: 70.5
# calculation: ((95-50)*0.75+50*0.5)+20%=70.5

# input: 120
# output: 93
# calculation: ((120-50)*0.75+50*0.5)+20%=93

# input:213
# output: 210.72
# #caculation: ((213-150)*1.2 + 100*0.75 + 50*0.5) + 20% = 210.72

# input: 348
# output: 440.4
# calculation: ((348-250)*1.50 + 100*1.2 + 100*0.75 + 50*0.5) + 20% = 440.4

# input: -2
# output: Not acceptable

# input: dfhajgfa
# output: Not acceptable

elec_unit = input("Input electricity unit: ")


if elec_unit.isdigit():
    input = int(elec_unit)
    if input <= 50:
        bill = input * 0.50 * 1.2
    elif input <= 150:
        bill = ((input - 50) * 0.75 + 50 * 0.5) * 1.2
    elif input <= 250:
        bill = ((input - 150) * 1.2 + 50 * 0.5 + 100 * 0.75) * 1.2
    else:
        bill = ((input - 250) * 1.5 + 50 * 0.5 + 100 * 0.75 + 100 * 1.2) * 1.2
    print(bill)

else:
    print("Not acceptable")
