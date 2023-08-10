# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import choice, randint

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def psevdoname_gen():
    rword = ''
    for _ in range(randint(4, 7)):
        rword += choice(VOWELS + CONSONANTS)
    return rword.capitalize()


def add_word(word: str, count_words: int):
    with open(word, 'w') as names_file:
        for _ in range(count_words):
            names_file.write(psevdoname_gen() + "\n")


if __name__ == '__main__':

    add_word('word_list.txt', 5)
