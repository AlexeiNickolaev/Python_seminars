# # Улучшаем задачу 2.
# # Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# # Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# # Для преобразования строковых аргументов командной строки
# # в числовые параметры используйте генераторное выражение.

# import sys
# import random


# def game_guess(low_lim=1, ap_lim=10, tryes=3):

#     res = random.randint(low_lim, ap_lim)
#     for i in range(tryes):
#         res_us = int(input(f'Введите число от {low_lim} до {ap_lim}: '))
#         if res == res_us:
#             print('Вы угадали')
#             return True
#         elif res > res_us:
#             print('Загаданное число больше')
#         else:
#             print('Загаданное число меньше')
#     else:
#         return False


# if __name__ == '__main__':
#     print(sys.argv)
#     task, low_lim, ap_lim, tryes = sys.argv
#     game_guess(int(low_lim), int(ap_lim), int(tryes))

import sys
import random


def game_guess(low_lim=1, ap_lim=10, tryes=3):
    res = random.randint(low_lim, ap_lim)
    for i in range(tryes):
        res_us = int(input(f'Введите число от {low_lim} до {ap_lim}: '))
        if res == res_us:
            print('Вы угадали')
            return True
        elif res > res_us:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
    else:
        return False


if __name__ == '__main__':
    args = sys.argv[1:]  # Пропустим первый элемент (имя скрипта)
    if len(args) >= 3:
        low_lim, ap_lim, tryes = map(int, args)
        game_guess(low_lim, ap_lim, tryes)
    else:
        print("Введите параметры: нижняя граница, верхняя граница, количество попыток.")
