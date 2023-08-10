# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


from task2 import add_word
from task1 import fill_numb
from typing import TextIO


def read_file(file: TextIO) -> str:
    text = file.readline()
    if not text:
        file.seek(0)
        text = file.readline()
    return text[:-1]


def get_file_len(filename):
    with open(filename, 'r') as f:
        return len(f.read().split('\n'))


def create_mult(file_names: str, file_numbers, result):

    len_names = get_file_len(file_names)
    len_numbs = get_file_len(file_numbers)
    max_file_len = max(len_names, len_numbs)

    with (open(file_names, 'r') as f_names,
          open(file_numbers, 'r') as f_numbs,
          open(result, 'w') as f_res):

        for i in range(max_file_len):
            num_1, num_2 = map(float, read_file(f_numbs).split('|'))
            names = read_file(f_names)
            mult = num_1 * num_2

            print(names, mult, max_file_len)
            if mult < 0:
                f_res.write(f'{names.lower()}\t{abs(mult)}\n')
            else:
                f_res.write(f'{names.upper()}\t{int(mult)}\n')


if __name__ == '__main__':
    word_name = 'word_list.txt'
    num_name = 'num_list.txt'

    fill_numb(num_name, 5)
    add_word(word_name, 10)
    create_mult(word_name, num_name, 'result.txt')
