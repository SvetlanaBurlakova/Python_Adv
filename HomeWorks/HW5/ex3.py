"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci():
    """Функция генератор чисел Фибоначчи"""
    n1, n2 = 0, 1
    yield n1
    yield n2
    while True:
        n1, n2 = n2, n1 + n2
        yield n2


n = int(input('введите кол-во чисел  Фибоначчи: '))

f = fibonacci()
for _ in range(n):
    print(next(f), end=' ')
