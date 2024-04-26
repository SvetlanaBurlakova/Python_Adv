"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json

def create_json_from_txt(file: str):
    with (
        open(file, 'r', encoding="utf-8") as txt_file,
        open('file1.json', 'w', encoding='utf-8') as json_file,
    ):
        data = txt_file.readlines()
        dct = {}
        for d in data:
            name, number = d.split(' ')
            dct[name.title()] = number.rstrip('\n')
        json.dump(dct, json_file, indent=3)


if __name__ == '__main__':
    create_json_from_txt('file1.txt')