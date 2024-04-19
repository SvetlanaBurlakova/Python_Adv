"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
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


if __name__ == '__main__':
    mistery = 'Зимой и летом одним цветом'
    answer_list = ['елка', 'ель']
    tries = 5
    print(mistery_tries(mistery, answer_list, tries))
