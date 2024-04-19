"""
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
(номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
"""

_guess_tries = {}

def mistery_tries(mistery: str, answers: list, tries: int) -> int:
    """Функция загадывает загадку и проверяет результат за Tries попыток"""
    count = 0
    print(f'Отгадайте загадку: {mistery}, у вас {tries} попыток')
    while count < tries:
        count += 1
        answer_str = input(f'Попытка {count}, ведите ответ: ')
        if answer_str.lower() in answers:
            result_tries(mistery, count)
            return None
    else:
        result_tries(mistery, 0)
        return None


def all_misteries(misteries: dict, tries):
    """Функция перебирает все заданные загадки"""
    for k,v in misteries.items():
        mistery_tries(k,v, tries)


def result_tries(mistery: str, answer:int):
    """Фугкция формирует словарь загадка: кол-во попыток на отгадывание"""
    _guess_tries[mistery] = answer


def print_result():
    """Вывод данных из словаря загадок"""
    for k,v in _guess_tries.items():
        print(f'Загадка {k}, отгадана с попытки {v}')


if __name__ == '__main__':
    misteries = {'Зимой и летом одним цветом': ['елка', 'ель'],
                 'Что было «завтра», а будет «вчера»?': ['сегодня']}
    tries = 5
    all_misteries(misteries, tries)

    print_result()
