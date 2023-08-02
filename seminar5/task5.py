# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

res = []
for i in range(1, 100):
    if i % 15 == 0:
        res.append('FizzBuzz')
    else:
        if i % 3 == 0:
            res.append('Fizz')
        else:
            if i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(i)
print(res)

res_gen = ['FizzBuzz' if i % 15 == 0 else
           'Fizz' if i % 3 == 0 else
           'Buzz' if i % 5 == 0 else
           i for i in range(1, 100)]
print(res_gen == res)