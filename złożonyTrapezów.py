from sympy import *

# Funkcja1: -1 całka 1 x^2 dx, n=5; Wynik: całka = 0.75

# Wzór trapezwów złożony
# a całka b f(x)dx = h ((f(a)+f(b))/2+ n-1 Sigma k=1 f(x h))
# R = -((b-a)h^2)/12 f''(epsilon)
# Epsilon należy do (a,b),   Epsilon = max f(x) a<=x<=b
# h = (b-a)/n n liczba przzedziałów N - n+1 - liczba węzłów

def trapez_zlozony():
    x = symbols('x') # symbole
    f = x**2 # wzor funkcji
    d_first = f.diff(x) # 1. pochodna
    d_second = d_first.diff(x) # 2. pochodna

    a = -1
    b = 1
    n = 4

    h = (b-a)/n

    if(a>b): max = a
    else: max = b

    fa = f.evalf(subs={x:a})
    fb = f.evalf(subs={x:b})
    f2 = d_second.evalf(subs={x:max})
    suma=0
    temp = a

    for k in range(1, (n)):
        temp += h
        suma += f.evalf(subs={x:temp})

    calka = h * (((fa + fb) / 2) + suma)
    R = -1 * (((b - a) * pow(h, 2)) / 12) * f2

    print(f"Całka = {calka}")
    print(f"R = {R}")

trapez_zlozony()
