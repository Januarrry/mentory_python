sum = 0


sum = sum + 5

number = 3

sum = number + sum


a = 5 + 2
a = 5
a = a + 4
a = 5
b = 7
c = a + b  # 5+7
c = c + a  # 12+5
c = c + 1  # 18

c = c + b  # 25

if a == 5:  # True
    b = a + 4  # a 5 b 9 c 25
    if b == 5:  # FAlse
        if a == 3:
            a = 5
        a = 40
        a = 50
        a = 10
    elif a == 10:
        a = 11
        a = 12
        b = c
    else:
        a = b + c  # 9+25 a34

    c = 21

    if c == 10:
        a = 5
        b = c
        c = a
    elif c == 5:
        a = 3
        b = 2
        c = 1
    else:
        a = b + c  # 9 +21 = a30

    c = a  # 30
else:
    if a == 1:
        a = b
        b = 2
        c = a

if c == 3:
    a = 11  # 30
    b = c  # 9
    c = 3  # 30

print(a)
print(b)
print(c)
