"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
директорий.
"""
import os
from pathlib import Path
import json
import csv
import pickle


def getsizeof_dir(directory: Path) -> int:
    """Функция расчитывает размер папки, с учетом всех содержащихся в ней файлов,
    даже если файла находятся в подпапках"""
    size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            p = Path(file)
            size += os.path.getsize((root / p))
    return size


def go_through_directory(directory: Path, file_name: str, structure: list) -> dict:
    """Функция создает словарь содержащий, путь до объекта, тип обекта и размер объекта"""
    dct = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            p = Path(file)
            size = os.path.getsize((root / p))
            dct[p.name] = {structure[1]: root,structure[2]: 'Файл', structure[3]: size}
        for dir in dirs:
            p = Path(dir)
            dct[p.name] = {structure[1]: root, structure[2]: 'Директория', structure[3]: getsizeof_dir((root / p))}

    save_to_json(dct, file_name)
    save_to_csv(dct, file_name, structure)
    save_to_pickle(dct, file_name)


def save_to_json(data: dict, file_name) -> None:
    """Функция записывает словарь в json файл"""
    name = file_name + '.json'
    with open(name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_to_csv(data: dict, file_name, fieldnames) -> None:
    """Функция записывает словарь в csv файл"""
    name = file_name + '.csv'
    with open(name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames,
                       quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for k,v in data.items():
            writer.writerow({fieldnames[0]: k,
                             fieldnames[1]: v[fieldnames[1]],
                             fieldnames[2]: v[fieldnames[2]],
                            fieldnames[3]: v[fieldnames[3]]})


def save_to_pickle(data: dict, file_name) -> None:
    """Функция записывает словарь в pickle файл"""
    name = file_name + '.pickle'
    with open(name, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    structure = ["Объект", "Родительская папка", "Тип объекта", "Размер"]
    go_through_directory(Path('dir'), 'result', structure)