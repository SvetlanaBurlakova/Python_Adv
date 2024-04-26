from HomeWorks.HW8 import ex7
from HomeWorks.HW8 import directory_info
from pathlib import Path

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ex7.csv_to_pickle('users_6.csv')
    structure = ["Объект", "Родительская папка", "Тип объекта", "Размер"]
    directory_info.go_through_directory(Path('dir'), 'result', structure)







