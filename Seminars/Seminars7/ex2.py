"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""
from string import ascii_lowercase
from random import randint, choice

def generate_file_name(file_name: str, n: int):
    letters = 'aeiouy'
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(n):
            is_corect = False
            while not is_corect:
                name = ''.join([l for _ in range(randint(4, 7)) for l in choice(ascii_lowercase)]).title()
                for el in name:
                    if el in letters:
                        is_corect = True
                        break
            print(name, file=f)


if __name__ == '__main__':
    generate_file_name('file2.txt', 7)