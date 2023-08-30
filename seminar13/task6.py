# Добавление пользователя.
# Если уровень пользователя меньше,
# чем ваш уровень, вызывайте исключение уровня доступа.

import task3
import task4

if __name__ == '__main__':
    p1 = task4.Project()
    p1.loan_data()
    print(p1.data)
    p1.enter('we', 2)
    u1 = task3.User('kk', 9, 8)
    p1.add_user(u1)
    print(p1.data)
