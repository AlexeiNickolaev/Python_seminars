# Доработаем задачи 2 и 3. Создайте класс проекта,
# который имеет следующие методы:
# * загрузка данных (функция из задания 3)

import task3


class Project:
    def __init__(self):
        self.data = []

    def loan_data(self):
        self.data = task3.load_json()

    def add_user(self, new_user):
        if new_user.level > self.user.level:
            self.data.append(new_user)
        else:
            raise task3.ErrorLevel
