"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from datetime import datetime
from calendar import isleap
from sys import argv

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
    if len(argv) < 2:
        print('Запустите программу еще раз и передайте дату в качестве аргумента: ')
    else:
        data = argv[1]
        if check_the_date(data):
            print(f'Дата: {data} существует')
        else:
            print(f'Дата: {data} не существует')