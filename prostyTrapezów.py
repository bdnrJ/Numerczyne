def f(x):
    return x ** 2


s = 0

xp = int(input("podja pocztek: "))

xk = int(input("podja koniec: "))

n = 100000

dx = (xk - xp) / n

for i in range(n):
    s = s + f(xp + i * dx)

s = (s + (f(xp) + f(xk) / 2)) * dx

print(s)
