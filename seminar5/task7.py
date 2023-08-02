# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def gen_simple(n):
    res = []
    for i in range(2, n):
        if is_simple(i):
            yield i
    return res


def is_simple(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(list(gen_simple(10)))

for i in gen_simple(20):
    print(i)
