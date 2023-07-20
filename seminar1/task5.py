# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = 10
e = 3
STEP = 2

count = 1
summ_nims = 0

while count <= n:
    if count % e != 0:
        summ_nims += count
        print(count, summ_nims)
    count += STEP

print(summ_nims)
