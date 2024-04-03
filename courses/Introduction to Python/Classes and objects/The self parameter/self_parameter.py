class Complex:
    num = 0
    r = 0
    i = 0

    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

    def build(self):
        self.num = complex(self.r, self.i)


complex_number = Complex()  # Instantiate a complex number object
complex_number.create(12, 5)  # Call create method with real_part = 12 and imag_part = 5
complex_number.build()  # Build the complex number
print(complex_number.num)


class Calculator:
    current = 0

    def add(self, amount):
        # Update the current attribute by adding the amount to it.
        self.current += amount

    def get_current(self):
        return self.current


my_value = Calculator()
my_value.add(10050066)
my_value.add(36645474)
my_value.add(11111)
print(my_value.get_current())

sky = Calculator()
sky.add(12)
sky.add(80)
sky.add(1222222)
print(sky.get_current())
