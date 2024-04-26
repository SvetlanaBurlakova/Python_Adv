"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import csv
import json

def create_json_from_csv(file_csv: str, file_json: str):
    with open(file_csv, 'r', encoding='utf-8') as f_csv:
        csv_reader = csv.reader(f_csv)
        dct = {}
        for i, line in enumerate(csv_reader):
            if i > 0:
                level = line[1]
                id_ = f'{line[0]:0>10}'
                name = line[2].title()
                st = id_ + name
                hash_ = hash(st)
                dct[level] = {id_: name, 'hash': hash_}
    with open(file_json, 'w', encoding='utf-8') as f_json:
        json.dump(dct, f_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    create_json_from_csv('users.csv', 'users_new.json')