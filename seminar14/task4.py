# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from task1 import clear_text
import pytest


def test_no_change():
    assert clear_text('some text') == 'some text'


def test_registre_change():
    assert clear_text('SoMe TexT') == 'some text'


def test_punctuation_delete():
    assert (clear_text('SoMe, TexT') == 'some text'), """Пунктуация\
- корявая. Поправь её"""


if __name__ == "__main__":
    pytest.main(['-v'])
