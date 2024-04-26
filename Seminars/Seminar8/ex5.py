"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых
pickle файлов.
"""
import pickle
import json
from pathlib import Path

def find_json_save_pickle(dir: Path):
    p = Path(dir)
    for obj in p.iterdir():
        if obj.is_file() and obj.suffix[1:] == 'json':
            name = obj.name
            with open(obj, 'r') as json_file:
                data = json.load(json_file)
            pickle_file_name = name.split('.')[0] + '.pickle'
            with open(pickle_file_name, 'wb') as f:
                pickle.dump(data, f)


if __name__ == '__main__':
    find_json_save_pickle(Path('.'))
