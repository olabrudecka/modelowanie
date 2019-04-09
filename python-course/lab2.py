from cs50 import get_int, get_float, get_string, get_char
from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from decimal import *
from sympy import *
#alternative way of reading inputs - using library:
#in terminal/command line write pip install cs50
#restart your IDE (Pycharm, VSCode, whatever it is)
#remember to use python3 in your project
#add "from cs50 import get_int" to the top of your file
# x = get_int("x: ")
# y = get_int("y: ")
"""

print("x:")
x = int(input())
print("y:")
y = int(input())

print("-"*10)
print(x + y)
print("-"*10)

print(f"x + y: {x + y}")
print(f"x - y: {x - y}")
print(f"x * y: {x * y}")
print(f"x / y: {x / y}")
print(f"x modulo y: {x % y}")
# """
# xIsEven = x % 2 == 0
# xIsEvenLog = 'X is even' if xIsEven else 'X is not even'
# print(xIsEvenLog)
#

#########1#########

def zadanie1():
    okrag1 = get_float('Podaj pierwszą średnicę: ')
    okrag2 = get_float('Podaj drugą średnicę:')

    obwod1 = 2 * pi * okrag1
    obwod2 = 2 * pi * okrag2
    pole1 = pi * (okrag1 ** 2)
    pole2 = pi * (okrag2 ** 2)
    print(f"pole pierwszego: {pole1}, obwod pierwszego: {obwod1}")
    print(f"pole drugiego: {pole2}, obwod drugiego: {obwod2}")

#zadanie1()

# ########2#########

def czy_parzysta(n):
    a = 0
    if n%2 != 0:
        print('Liczba musi być parzysta')
        a = 1
    return a

def zadanie2():
    a = 0
    print('Znajdź liczby x i y, które spełniają wymagania: x jest podzielne przez y, obie liczby są parzyste.')
    x = get_float("podaj x: ")
    y = get_float("podaj y: ")
    while y == 0:
        print('Druga liczba nie może być równa 0')
        y = get_float("podaj y: ")


    while (x % y != 0 or x % 2 != 0 or y % 2 != 0):
        print('Podaj inne liczby')
        x = get_float("podaj x: ")
        y = get_float("podaj y: ")
        while y == 0:
            print('Druga liczba nie może być równa 0')
            y = get_float("podaj y: ")
    print(f"{x} jest podzielne przez {y} i obie wartości są parzyste")

#zadanie2()


########3########
def zadanie3():
    x = get_float("podaj x: ")
    y = get_float("podaj y: ")
    while y == 0:
        print('Druga liczba nie może być równa 0')
        y = get_float("podaj y: ")

    print('x jest podzielna przez y' if x % y == 0 else 'x nie jest podzielna przez y')

#zadanie3()
########4#########

def zadanie4():
    x = get_float("podaj x: ")
    y = get_float("podaj y: ")
    while y == 0:
        print('Druga liczba nie może być równa 0')
        y = get_float("podaj y: ")
    b = int(x/y)
    b = Decimal(b)
    print(round(b,2))

#zadanie4()

#########5#########

def zadanie5():


    s = get_float('Podaj liczbę: ')
    x_knots = np.linspace(-s * sin(s*10), s * sin(s*10), 201)
    y_knots = np.linspace(-s * sin(s*10), s * sin(s*10), 201)
    X, Y = np.meshgrid(x_knots, y_knots)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.cos(R) ** 2 * np.exp(-0.1 * R)
    ax = Axes3D(plt.figure(figsize=(8, 5)))
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
    plt.show()

#zadanie5()
x = Symbol('x')
y = sin(x)
print(y.diff(x))
# TASKS (8p)- calculate & print:
#0 Use alternative way of reading inputs - using library (0.5p)
#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)

