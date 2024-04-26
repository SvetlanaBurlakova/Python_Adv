"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json
from pathlib import Path

def update_access_users(db_file: str):
    f = Path(db_file)
    if f.exists():
        with open(db_file, 'r', encoding='utf-8') as f:
            dct = json.load(f)
            ids = [k1 for k,v in dct.items() for k1 in v]
            print(dct)
            print(ids)
    else:
        dct = {}
        ids = []
    while True:
        name = input('введите имя: ')
        ident = input('введите id: ')
        while ident in ids:
            ident = input('введите id: ')
        ids.append(ident)
        level = input('введите уровень: ')
        dct[level] = dct.get(level, {}) | {ident:name}
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(dct, f, indent=4)


if __name__ == '__main__':
    update_access_users('users.json')