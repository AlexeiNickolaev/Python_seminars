# Создайте декоратор с параметром.
# Параметр - целое число,
# количество запусков декорируемой функции.

from task3 import json_logging
from functools import wraps

# def many_launch(count: int):
#     def deco(func: callable):
#         def wrapper(*args, **kwargs):
#             res_list = []
#             for _ in range(count):
#                 res_list.append(func(*args, **kwargs))
#             return res_list
#         return wrapper
#     return deco


def many_launch(count: int):
    def deco(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res_list = []
            for s_c in range(count):
                res_list.append(func(*[i for i in range(s_c)], **kwargs))
            return res_list
        return wrapper
    return deco


@json_logging  # Поменяли местами, вернулся wrapper.json
@many_launch(10)  # Поменяли местами, вернулся wrapper.json
def sum_args_v1(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    print(sum_args_v1(2, 4, 6, 8, 10,  key='Hello'))
