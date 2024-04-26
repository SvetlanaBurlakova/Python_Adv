"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle

def csv_to_pickle(csv_file):
    with open(csv_file, 'r') as f_csv:
        data = csv.reader(f_csv, delimiter=',')
        dct = {}
        for i, line in enumerate(f_csv):
            if i > 0:
                dct[line[1]] = {line[0]: line[2]}

    print(pickle.dumps(dct))


if __name__ == '__main__':
    csv_to_pickle('users_6.csv')