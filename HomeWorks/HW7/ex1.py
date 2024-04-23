"""
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
from pathlib import Path

def group_files_rename(directory: Path, end_file: str, digits: int, extention_before: str,
                       extention_after: str, name_range: list) -> None:
    """Функция переименовывает файлы из каталога"""
    num = 1
    for obj in directory.iterdir():
        if obj.is_file() and obj.suffix[1:] == extention_before:
            number = f'{num:0>{digits}}'
            new_name = obj.name[name_range[0]: name_range[1]] + end_file + number + '.' + extention_after
            Path.rename(obj, (directory / new_name))
            num += 1


if __name__ == '__main__':
    group_files_rename(Path('dir'), end_file='_file_',digits=3,
                       extention_before='txt', extention_after='doc',
                       name_range=[3, 6])