"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

def mistery_tries(mistery: str, answers: list, tries: int) -> int:
    """Функция загадывает загадку и проверяет результат за Tries попыток"""
    count = 0
    print(f'Отгадайте загадку: {mistery}, у вас {tries} попыток')
    while count < tries:
        count += 1
        answer_str = input(f'Попытка {count}, ведите ответ: ')
        if answer_str.lower() in answers:
            return count
    else:
        return 0


def all_misteries(misteries: dict, tries):
    """Функция перебирает все заданные загадки"""
    for k,v in misteries.items():
        print(mistery_tries(k,v, tries))


if __name__ == '__main__':
    misteries = {'Зимой и летом одним цветом': ['елка', 'ель'],
                 'Что было «завтра», а будет «вчера»?': ['сегодня']}
    tries = 5
    all_misteries(misteries, tries)