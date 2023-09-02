# Создайте функцию,
# которая удаляет из текста все символы кроме
# букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters

LETTERS = set(ascii_letters) | {' '}


def clear_text(text: str) -> str:
    return ' '.join(''.join(i for i in text if i in LETTERS).lower().split())


print(clear_text('Some text 123, 123 exmpl'))
