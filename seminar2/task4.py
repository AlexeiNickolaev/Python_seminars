#  Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math
decimal.getcontext().prec = 42


def calc(d):
    pi = decimal.Decimal(math.pi)
    square = pi * (d/2)**2

    length_circle = pi*d
    return square, length_circle


d: decimal.Decimal = decimal.Decimal(input("Введите диаметр круга: "))

res = calc(d)
print(f'Площадь круга: {res[0]}, Длина окружности: {res[1]}')
