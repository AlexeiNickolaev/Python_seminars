# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня, ошибка доступа, ошибка проекта

import json


class ProjectException(Exception):
    pass


class ErrorLevel(ProjectException):
    pass


class ErrorPermition(ProjectException):
    pass


class User:
    def __init__(self, name, id, level=0) -> None:
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, __value: "User") -> bool:

        return self.id == __value.id and self.name == __value.name

    def __repr__(self) -> str:
        return f'User {self.name} {self.id} {self.level}'


def load_json():
    try:
        with open('data_base.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    result = []
    for level, value in data.items():
        for user in value:
            name, id = user.values()
            result.append(User(name=name, id=id, level=int(level)))
    return result
