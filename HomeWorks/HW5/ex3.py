"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci(n=0, n1=0, n2=1):
    """Функция генератор чисел Фибоначчи"""
    while True:
        if n == 0:
            n += 1
            yield n1
        if n == 1:
            n += 1
            yield n2
        n1, n2 = n2, n1 + n2
        yield n2


n = int(input('введите кол-во чисел  Фибоначчи: '))

f = fibonacci()
for _ in range(n):
    print(next(f), end=' ')
