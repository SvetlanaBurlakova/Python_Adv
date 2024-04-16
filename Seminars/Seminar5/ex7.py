"""
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу
и на себя».
"""
def prime(number: int) -> bool:
    if number < 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_simple():
    count = 2
    while True:
        if prime(count):
            yield count
        count += 1

j = generate_simple()
for _ in range(int(input("введите число N: "))):
    print(next(j), end=' ')
