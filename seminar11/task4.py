# Доработаем класс Архив из задачи 3.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    """is archive"""
    instance = None

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __new__(cls, text, numb):
        if cls.instance:
            cls.instance.arch_txt.append(cls.instance.text)
            cls.instance.arch_numb.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.arch_txt = []
            cls.instance.arch_numb = []
        return cls.instance

    def __str__(self):
        return f'Метод класса: Archive, текущий текст: {self.text}, текущее число: {self.number}'

    def __repr__(self):
        return f'Archive {self.text, self.number}'


a1 = Archive('qwerty', 32)
a2 = Archive('asdfg', 23)
print(a2.instance.arch_txt, a2.instance.arch_numb)
print(Archive.__doc__)
print(a1, repr(a1))
