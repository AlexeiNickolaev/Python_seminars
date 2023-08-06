# Добавьте в модуль с загадками функцию, которая принимает
# на вход строку (текст загадки) и число (номер попытки, с которой она угадана)
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

def riddle_game(riddle="Зимой и летом одним цветом",
                riddle_ans=["Елка", "Eжик", "Зима"],
                tryes=3):
    for i in range(tryes):
        word = input(f"Отгадайте загадку - {riddle}")
        if word in riddle_ans:
            return i

    return 0


def add_dict_game():


dict_game = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
                 'Не лает, не кусает, в дом не пускает': ['замок'],
                 'Сидит дед во сто шуб одет': ['лук', 'луковица'], }


for key, value in dict_game.items():
    _func(riddle_game(key, value, tryes=5), key)

_dict = {}


def _func(attempt: int, riddle: str):

    _dict.update({riddle: attempt})


def _show_result():

    for key, value in _dict.items():
        print(key, value)


if __name__ == "__main__":
    add_dict_game()
_show_result()
