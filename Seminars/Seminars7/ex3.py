"""
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""
def read_line_or_begin(fd) -> str:
    """Функция возвращает сроку, либо переходит на начало файла и читает файл снова"""
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def generate_file_from_existing_files():
    """Создает новый файл на основе двух файлов"""
    with (
            open('file1.txt', 'r', encoding='utf-8') as f1,
            open('file2.txt', 'r', encoding='utf-8') as f2,
            open('file3.txt', 'w', encoding='utf-8') as f3
    ):
        lst1 = f1.readlines()
        lst2 = f2.readlines()
        len1, len2 = len(lst1), len(lst2)
        min_size, max_size = min(len1, len2), max(len1, len2)
        for i in range(max_size):
            l1 = read_line_or_begin(f1)
            l2 = read_line_or_begin(f2)
            mlt = int(l1.split('|')[0]) * float(l1.split('|')[1])
            if mlt < 0:
                print(f'{l2.lower().rstrip('\n')} {abs(mlt)}', file=f3)
            else:
                print(f'{l2.upper().rstrip('\n')} {round(mlt, 0)}', file=f3)


if __name__ == '__main__':
    generate_file_from_existing_files()