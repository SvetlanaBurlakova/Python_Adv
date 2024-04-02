"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки.
"""
from random import randint

TRIES = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

number = randint(LOWER_LIMIT, UPPER_LIMIT)

while TRIES > 0:
    guess_number = int(input('Введите число: '))
    print(f'Попытка {10 - TRIES + 1}:', end=' ')
    if guess_number == number:
        print(f'Вы угадали число {number}!')
        break
    elif guess_number < number:
        print(f'Загаданное число больше')
    else:
        print('Загаданное число меньше')
    TRIES -= 1
else:
    print('Извините, но попытки закончились')
