"""
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён
"""
from string import ascii_lowercase
from random import randint, choice
from pathlib import Path


def generate_text(min_length=6, max_length=30):
    """Генерация файла"""
    return ''.join([l for _ in range(randint(min_length, max_length)) for l in choice(ascii_lowercase)])


def create_file(extention: str, directory: str, min_length=6, max_length=30, min_bytes=256, max_bytes=4096, files_count=42):
    """Создание файлов"""
    if not Path(directory).is_dir() or not Path(directory):
        Path(directory).mkdir()
    for _ in range(files_count):
        file = generate_text(min_length, max_length) + '.' + extention
        file_name = Path().cwd() / directory / file
        while True:
            try:
                with open(file_name, 'bw') as f:
                    f.write(generate_text(min_bytes, max_bytes).encode('utf-8'))
            except:
                file = generate_text(min_length, max_length) + '.' + extention
                file_name = Path().cwd() / directory / file
            else:
                break


if __name__ == '__main__':
    create_file('rnd','dir', max_length=10, files_count=2)
