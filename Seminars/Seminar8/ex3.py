"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""
import csv
import json

def save_csv(filename):
    with open(filename, 'r', encoding='utf-8') as json_file:
        dct = json.load(json_file)
    headers = ['id', 'level', 'name']
    with open('users.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers,)
        writer.writeheader()
        for k, v in dct.items():
            for k1, v1 in v.items():
                writer.writerow({'id': k1, 'level': k, 'name': v1})



if __name__ == '__main__':
    save_csv('users.json')