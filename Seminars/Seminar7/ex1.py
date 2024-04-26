"""
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""
from random import randint, uniform

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def file_with_numbers(n: int, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(n):
            print(f'{randint(MIN_NUMBER, MAX_NUMBER)}|{uniform(MIN_NUMBER, MAX_NUMBER)}', file=f)


if __name__ == '__main__':
    n = int(input('Введите кол-во строк: '))
    file_with_numbers(n, 'file1.txt')
