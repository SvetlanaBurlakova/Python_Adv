"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
"""
names = ['Alice', 'Bob', 'Charlie']
rates = [10, 20, 30]
procents = ['10.1%', '5.3%', '6.2%']

print({name: rate * float(procent[:-1]) / 100 for name, rate, procent in zip(names, rates, procents)})
