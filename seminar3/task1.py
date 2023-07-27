#  Вручную создайте список с целыми числами, которые
#  повторяются. Получите новый список, который содержит
#  уникальные (без повтора) элементы исходного списка.

# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

nums = [1, 1, 2, 2, 3, 4, 5, 5]
res = list(set(nums))

print(res)

temp = []
for value in nums:
    if value not in temp:
        temp.append(value)
print(temp)
