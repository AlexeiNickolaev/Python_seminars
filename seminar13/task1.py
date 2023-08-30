# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def correct_input_float():

    while True:
        number = input("Введите число: ")
        try:
            return float(number)
        except ValueError:
            print("Введено НЕ число")


if __name__ == '__main__':
    correct_input_float()
