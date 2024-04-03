import functions.goodbye as bye
from functions.greeting import hello
from classes import calculator
# Import the `official` module here
from functions.greeting import official
from functions.goodbye import good_bye
print(hello.hello('Susan'))
print(good_bye('Alex'))

c = calculator.Calculator()
c.add(2)
c.multiply(10)
print(c.get_current())

print(official.hello('Sam'))
