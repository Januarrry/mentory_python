# Import class Calculator from another module
from my_module import hello as hey
# import calculator
from calculator import Calculator, Calculator1
print(hey("User"))

calc = Calculator()  # Name `Calculator` used directly without prefix `calculator`
calc.add(2)
calc.multiply(100)
calc.divide(3)

hjkkjhhjkhjhjk = Calculator1()  # Name `Calculator` used directly without prefix `calculator`
print(calc.get_current())



