"""
Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""
def sort_bubbles(numbers: list) -> list:
    """Сортировка пузырьком на месте"""
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == '__main__':
    print(sort_bubbles([3, 6, 2, 1, 7, 2]))
