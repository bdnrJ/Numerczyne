# Definiujemy funkcję
def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x - 7


# Twierdzenie Bolzano-Cauchy'ego
def twBolzanoCauchyego(x0, x1):
    # Czy f(x0)*f(x1) < 0 ?
    twierdzenie = f(x0) * f(x1)
    if (twierdzenie < 0):
        return True
    else:
        return False


# wzór: xk = xk-1 - [(f(xk-1)(xk-1 - xk-2))/f(xk-1) - f(xk-2)]
def obliczenia():
    # Zmienna wykorzystywana do sprawdzenia po którym razie program się zakończy
    n = 2

    # Definiujemy epsilon
    epsilon = float(input("Podaj epislon (ε):"))

    # Definiujemy granice przedziału [x0,x1]
    x0 = int(input("Podaj początek przedziału (x0): "))
    x1 = int(input("Podaj koniec przedziału (x1): "))

    # Sprawdzamy czy spełnione jest twierdzenie Bolzano-Cauchy'ego
    if (twBolzanoCauchyego(x0, x1)):

        # xk1 rozumiemy jako xk-1
        xk1 = x1
        # xk2 rozumiemy jako xk-2
        xk2 = x0

        while (True):
            # Korzystamy ze wzór: xk = xk-1 - [(f(xk-1)(xk-1 - xk-2))/f(xk-1) - f(xk-2)]
            xk = xk1 - ((f(xk1) * (xk1 - xk2)) / (f(xk1) - f(xk2)))
            # print("Wynik dla x" + str(n) + " = " + str(xk))
            # print(abs(f(xk)))
            if (abs(f(xk)) < epsilon):
                print("Wynik dla x" + str(n) + " = " + str(round(xk, 2)))
                return abs(round(f(xk), 5))
            else:
                # xk-2 = xk-1
                xk2 = xk1
                # xk-1 = xk
                xk1 = xk
                n = n + 1

    else:
        print("Twierdzenie Bolzano-Cauchy'ego nie jest spełnione")


# Wypisujemy wynik programu
print(obliczenia())
