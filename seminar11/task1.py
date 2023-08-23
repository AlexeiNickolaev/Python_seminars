# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now()
        return instance


ms1 = MyStr('some text', 'Alexei')
print(ms1, ms1.author)
print(ms1.time)
