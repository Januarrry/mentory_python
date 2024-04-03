# Write a program to calculate profit or loss. input 1 buy price, input 2 sell price
# Profit or loss = Revenue - Cost:
#   if resul is positive its profit, if result is negative its loss
# input 1 its price of buy goods, input 2 sell price
# if buy price lower than sell price: its profit
# if buy price higher than sell price or equal: its loss
## Rules:
# Only positive numbers are acceptable for both inputs
# output = input2 - input1,
#   if result is positive in terminal will show: "Your profit is" + output
#   if result is negative in terminal will show: "Your loss is " + output

## Test:
# input1: 100
# input2: 120
# output: "Your profit is 20"

## Test:
# input1: 100
# input2: 100
# output: "Neutral 0"

#
# input1: 120
# input2: 100
# output: "Your loss is 20%"
#
# input1: -200
# input2: 0
# output: Not acceptable
#
# input1: sdfg
# input2: 0
# output: Not acceptable
#
# input1: 100
# input2: fbfgbsl
# output: Not acceptable

# feedback
# rules should apply for all possible input
# what about can not acceptable be simplified
# 1 rule for 1 output
# can add % of loss or profit

user_input1 = input("Type buy price: ")
user_input2 = input("Type your sell price: ")

if user_input2.isdigit() and user_input1.isdigit():
    sell_price = int(user_input2)
    buy_price = int(user_input1)

    output = (sell_price - buy_price) / sell_price * 100
    if output < 0:
        output = output * (-1)
    output_str = str(output)
    if sell_price < buy_price:
        result = "Your loss is " + output_str + "%"
    elif sell_price > buy_price:
        result = "Your profit is " + output_str + "%"
    elif buy_price == sell_price:
        result = "Neutral " + output_str
    print(result)
else:
    print("Not acceptable")
