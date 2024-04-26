"""
Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым. Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""
from Seminars.Seminar7 import ex4

def generate_files_with_different_ext(dir_ext: dict):
    for k,v in dir_ext.items():
        ex4.create_file(k, 'dir' + '_' + str(k), files_count=v)


if __name__ == '__main__':
    generate_files_with_different_ext({'txt': 2, 'png': 1, 'doc': 3})