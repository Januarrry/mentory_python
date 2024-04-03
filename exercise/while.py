import week

print(week.user_input)


class Mylesson:
    spanish = 31
    inglesa = 42

    def foo(self):
        print(f"Yo y Kobi habla espaniol {self.spanish} días")
        print(f"and the rest is {self.inglesa} days english ")


object = Mylesson()
object.foo()
print(object.spanish)


class Hugs:
    per_day = 4

    def add(self, times):
        self.per_day += times


days = Hugs()
days.add(31)
days.add(20)
print(days.per_day)
