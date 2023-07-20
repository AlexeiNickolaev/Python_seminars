# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = 2021

MAIN_CRIT = 4
EXCLUDE_CRIT = 100
ADDITIONAL_CRIT = 400

if (year % MAIN_CRIT == 0
        and year % EXCLUDE_CRIT != 0
        or year % ADDITIONAL_CRIT == 0):

    print(True)
else:
    print(False)
