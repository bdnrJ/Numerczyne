def f(x):
    return x**2

s = 0

st = 0

xp = int(input("podja pocztek: "))

xk = int(input("podja koniec: "))

n = 10000

dx = (xk - xp) / n

for i in range(1,n+1):
    x = xp + i + dx
    st = st + f(x - (dx/2))
    s = s + f(x)

s = (dx / 6)*(f(xp) + f(xk) + 2*s + 4 * st)

print(s)