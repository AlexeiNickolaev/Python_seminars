# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def fill_numb(name, count_str):
    with open(name, 'w') as f:
        for _ in range(count_str):
            f.write(f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n')


if __name__ == '__main__':
    fill_numb('file_txt', 50)
