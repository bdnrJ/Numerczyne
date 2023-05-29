import numpy as np
import sympy as sp


def bisection(f, a, b, epsilon, maxiter):
    if f(a) * f(b) > 0:
        raise ValueError("te same krance")
    n = 0
    while n < maxiter:
        c = (a + b) / 2
        if abs(f(c)) < epsilon:
            print(f"Iteracja: {n}")
            print(f"Punkt Srodkowy: {c}")
            print(f"Funkcja z c: {f(c)}")
            return c, n
        if f(a) * f(c) < 0:
            print(f"Iteracja: {n}")
            print(f"Punkt Srodkowy: {c}")
            print(f"Funkcja z c: {f(c)}")
            b = c
        else:
            print(f"Iteracja: {n}")
            print(f"Punkt Srodkowy: {c}")
            print(f"Funkcja z c: {f(c)}")
            a = c
        n += 1
    raise RuntimeError("100 iteracji")


def f(x):
    return (x + 1) * pow((x - 1), 4)


a = -1.5
b = -0.75
epsilon = 0.1
maxInter = 1000
c = 0
fc = 0

x, n = bisection(f, a, b, epsilon, maxInter)