from sympy import *


# trapez_zlozony()

# Simpsona złożony
# Sn(f)=1/3*h(f(a)+f(b)+4* n Sigma k=1 f(x 2k-1)+2 n-1 Sigma k=1 f(x 2k))
# R = -((b-a)h^4)/180 * f''''(Epsilon)
# Epsilon należy do (a,b)

def simpson_zlozony():
    x = symbols('x')  # symbole
    f = x ** 2  # wzor funkcji
    d_first = f.diff(x)  # 1. pochodna
    d_second = d_first.diff(x)  # 2. pochodna
    d_third = d_second.diff(x)  # 3. pochodna
    d_fourth = d_third.diff(x)  # 4. pochodna

    a = -1
    R = 1
    n = 4
    h = (R - a) / n

    if (a > R):
        max = a
    else:
        max = R

    fa = f.evalf(subs={x: a})
    fb = f.evalf(subs={x: R})
    f4 = d_fourth.evalf(subs={x: max})

    suma_parzystych = 0
    suma_nieparzystych = 0
    temp = a

    for k in range(1, n):
        temp += h
        if (k % 2 == 0):
            suma_parzystych += f.evalf(subs={x: temp})
        else:
            suma_nieparzystych += f.evalf(subs={x: temp})

    suma_parzystych *= 2
    suma_nieparzystych *= 4

    s = (1 / 3) * h * (fa + fb + suma_nieparzystych + suma_parzystych)
    R = f4 * -1 * ((R - a) * pow(h, 4) / 180)

    print(f"Sn = {s}")
    print(f"R = {R}")


simpson_zlozony()
