"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import pickle
import csv

def pickle_to_csv(pickle_file):
    with open(pickle_file, 'rb') as f_p:
        data = pickle.load(f_p)
    headers = ['id', 'level', 'name']
    with open('users_6.csv', 'w', encoding='utf-8', newline='') as f_w:
        writer = csv.DictWriter(f_w, fieldnames=headers)
        writer.writeheader()
        for k, v in data.items():
            for k1, v1 in v.items():
                writer.writerow({'id': k1, 'level': k, 'name': v1})


if __name__ == '__main__':
    pickle_to_csv('users.pickle')