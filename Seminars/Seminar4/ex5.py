"""
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""
def calculate_bonus(names: list[str], rates: list[int], procents: list[str]) -> dict:
    """Возвращает премию"""
    return {name: rate * float(procent[:-1]) / 100 for name, rate, procent in zip(names, rates, procents)}


if __name__ == '__main__':
    names = ['Alice', 'Bob', 'Charlie']
    rates = [10, 20, 30]
    procents = ['10.1%', '5.3%', '6.2%']
    print(calculate_bonus(names, rates, procents))