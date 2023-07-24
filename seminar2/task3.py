#  Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def binary_func(number: int, n: int = 2):
    binary_number = ''
    while number != 0:
        result = str(number % n)
        binary_number = result + binary_number
        number //= n
    return binary_number


number: int = int(input("Введите целое число: "))
system_number: int = int(input("Введите систему исчисления: "))
print(binary_func(number, 8))

print(oct(number)[2:])
