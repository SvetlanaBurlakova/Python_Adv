"""
3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
from random import choice

def is_beat_queen(q1: list, q2: list) -> bool:
    """Функция проверяет бьют ли ферзи друг друга"""
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def all_queens(queens: list) -> bool:
    """Функция определяет бьют ли ферзи друг друга"""
    for i in range(len(queens) - 1):
        for j in range(i + 1, len(queens)):
            if is_beat_queen(queens[i], queens[j]):
                return False
    return True


def setup_queens(count: int) -> list:
    """Расстановка 8 ферзей в случайном порядке"""
    num = 0
    result = []
    while num < count:
        queens = [[i] for i in range(1, 9)]
        variants = [i for i in range(1, 9)]
        for q in queens:
            k = choice(variants)
            variants.remove(k)
            q.append(k)
        queens = [tuple(q) for q in queens]
        if all_queens(queens):
            if queens not in result:
                result.append(queens)
                num += 1
    return result


if __name__ == '__main__':
    # queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
    queens = [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)]
    print(all_queens(queens))

    variants = setup_queens(count=4)
    for variant in variants:
        print(variant)