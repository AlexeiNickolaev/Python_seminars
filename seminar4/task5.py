# Функция принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида "10.25%".
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения
# Сумма расчитывается как ставка умножения на процент премии

def get_bonuses(names, salarys, bonuses):
    bonus_dict = {}
    for name, salary, bonus in zip(names, salarys, bonuses):
        bonus_dict[name] = salary * float(bonus[: -1]) / 100
    return bonus_dict


names = ['Alexei', 'Andrey', 'Vladimir']
salarys = [100000, 850000, 900000]
bonuses = ['0.9%', '10.25%', '11.5%']

print(get_bonuses(names, salarys, bonuses))
