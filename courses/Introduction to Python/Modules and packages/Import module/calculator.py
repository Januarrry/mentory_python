"""
This module contains Calculator class
"""


class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current


class Calculator1:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

def test():
    print(" test")