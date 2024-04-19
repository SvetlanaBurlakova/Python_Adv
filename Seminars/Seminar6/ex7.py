"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
from datetime import datetime
from calendar import isleap

def check_the_date(data):
    try:
        d = datetime.strptime(data, '%d.%m.%Y')
        print(_leap_year(d.year))
        return True
    except:
        return False

def _leap_year(year):
    if isleap(year):
        return 'високосный'
    else:
        return 'не високосный'

if __name__ == '__main__':
    data = input('Введите дату в фомате DD.MM.YYYY: ')
    if check_the_date(data):
        print(f'{data} существует')
    else:
        print(f'{data} не существует')