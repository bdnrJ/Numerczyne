import math


def f(x):
    return x**2
    # return math.sin(x)

s = 0

xp = int(input("podaj pocztek"))

xk = int(input("podja koniec"))

n = 1000

dx = (xk - xp) / n

for i in range(n):
    x = xp + i * dx
    s = s + f(x)


s = s * dx
print(s)
