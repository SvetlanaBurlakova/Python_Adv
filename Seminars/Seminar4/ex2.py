"""
Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""
def create_list(stroka: str):
    """Возвращает список кодов Unicode"""
    return list(map(ord, sorted(set(stroka), reverse=True)))


if __name__ == '__main__':
    print(create_list(input('Введите текст: ')))