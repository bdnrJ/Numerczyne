import sympy as sp


# Definiujemy funkcję
def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x - 7


# Twierdzenie Bolzano-Cauchy'ego
def twBolzanoCauchyego(a, b):
    # Czy f(a)*f(b) < 0 ?
    twierdzenie = f(a) * f(b)
    if (twierdzenie < 0):
        return True
    else:
        return False


# Liczymy pochodną I stopnia:
def pochodne():
    # Definiujemy zmienną symboliczną
    x = sp.Symbol('x')

    # Obliczamy pochodną funkcji f
    df = sp.diff(f(x), x)

    # Zwracamy wynik
    return df


# Liczymy pochodną II stopnia:
def pochodne2():
    # Definiujemy zmienną symboliczną
    x = sp.Symbol('x')

    # Obliczamy pochodną funkcji f
    df = sp.diff(pochodne(), x)

    # Zwracamy wynik
    return df


# Sprawdzamy czy:
# f'(x0) * f''(x0) > 0
def sprawdzenie(a, b):
    x = sp.Symbol('x')

    f_valueA = f(a)
    df_valueA = pochodne().subs(x, a)
    df_valueA2 = pochodne2().subs(x, a)

    f_valueB = f(b)
    df_valueB = pochodne().subs(x, b)
    df_valueB2 = pochodne2().subs(x, b)

    # print(f_valueA)
    # print(df_valueA)
    # print(df_valueA2)
    #
    # print(f_valueB)
    # print(df_valueB)
    # print(df_valueB2)

    # Czy: f'(a) * f''(a) > 0  i Czy: f(a) * f''(a) > 0
    if (df_valueA * df_valueA2 > 0 or df_valueB * df_valueB2 > 0):
        return True
    else:
        return False


# wzór: xn+1 = xn-1 - [(f(xn-1) * (x0 - xn-1))/f(x0) - f(xn-1)]
# wzór: xn = a - [(f(a) * (b - a ))/(f(b) - f(a))]
def obliczenia():
    # Zmienna wykorzystywana do sprawdzenia po którym razie program się zakończy
    n = 1

    x = sp.Symbol('x')

    # Definiujemy epsilon
    epsilon = float(input("Podaj epislon (ε):"))

    # Definiujemy granice przedziału [a,b]
    a = int(input("Podaj początek przedziału (a): "))
    b = int(input("Podaj koniec przedziału (b): "))

    # Sprawdzamy czy spełnione jest twierdzenie Bolzano-Cauchy'ego
    if (twBolzanoCauchyego(a, b)):
        if (sprawdzenie(a, b)):

            while (True):
                xn = round(a - ((f(a) * (b - a)) / (f(b) - f(a))), 3)
                # print("Wynik dla x" + str(n) + " = " + str(xn))
                # print(abs(f(xn)))
                if (abs(f(xn)) < epsilon):
                    print("Wynik dla x" + str(n) + " = " + str(round(xn, 2)))
                    return abs(round(f(xn), 2))
                else:
                    a = xn
                    n = n + 1

        else:
            print("Sprawdzenie dla obydu granic przedziału jest fałszywe")
    else:
        print("Twierdzenie Bolzano-Cauchy'ego nie jest spełnione")


# Wypisujemy wynik programu
print(obliczenia())
