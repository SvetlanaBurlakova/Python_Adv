"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж
из трёх элементов: путь, имя файла, расширение файла.
"""
from os import path

def parse_path(path_str: str) -> tuple:
    "Функция возвращает путь, имя файла и расширение по переданному пути"
    path_to_file = path.dirname(path_str)
    full_name = path.basename(path_str)
    file_name = path.splitext(full_name)[0]
    extention = path.splitext(full_name)[1]
    return path_to_file, file_name, extention

file_info = parse_path(r'C:\Users\OneDrive\Рабочий стол\GB\Python\HW.py')
print(f'Путь: {file_info[0]}')
print(f'Имя файла: {file_info[1]}')
print(f'Расширение файла: {file_info[2]}')
