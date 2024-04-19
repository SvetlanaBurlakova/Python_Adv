"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
from random import randint


def guess_number(lower_limit=1, upper_limit=10, count=5):
    number = randint(lower_limit, upper_limit)
    tries = 1
    while tries <= count:
        guess_number = int(input('Введите число: '))
        print(f'Попытка {tries}:', end=' ')
        if guess_number == number:
            return True
        elif guess_number < number:
            print('Больше')
        else:
            print('Меньше')
        tries += 1
    else:
        return False


if __name__ == '__main__':
    lower_limit = int(input('Введите нижнюю границу: '))
    upper_limit = int(input('Введите верхнюю границу: '))
    count = int('Введите количетсво попыток: ')
    print(guess_number(lower_limit, upper_limit, count))
