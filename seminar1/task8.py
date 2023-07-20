# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = 5
STAR = '*'
SPACE = ' '
start = 1
stop = rows + 1

for row in range(start, stop):
    stars = STAR * (row * 2 - 1)
    spaces = SPACE * (rows - row)
    print(spaces + stars)
