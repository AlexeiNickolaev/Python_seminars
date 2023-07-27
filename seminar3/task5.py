# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

# [7, 10, 3, 8, 3] -> [1, 3, 5]


nums = [7, 10, 3, 8, 3]
nums_2 = []

# for i in range(len(nums)):
#     if nums[i] % 2 != 0:
#         nums_2.append(i + 1)
# print(nums_2)

for indx, num in enumerate(nums, start=1):
    if num % 2 != 0:
        nums_2.append(indx)
print(nums_2)
