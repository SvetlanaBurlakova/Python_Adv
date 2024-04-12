"""
Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""
def sum_in_range(numbers: list[int], start: int, end: int) -> int:
    """Расчет суммы чисел между двумя индексами"""
    if start > end:
        start, end = end, start
    if start < 0:
        start = 0
    if end > len(numbers) - 1:
        end = len(numbers) - 1
    return sum(numbers[start:end + 1])


if __name__ == '__main__':
    print(sum_in_range([1, 2, 3, 4, 5, 6, 7], 5, 3))