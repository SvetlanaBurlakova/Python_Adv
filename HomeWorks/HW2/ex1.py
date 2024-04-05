"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
BASE = 16

def get_hex_value(rem_div):
    dct_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if rem_div >= 10:
        return dct_hex[rem_div]
    else:
        return str(rem_div)

number_to_convert = int(input('Введите число: '))

print(f'Проверка: {hex(number_to_convert)}')

result = ''

while number_to_convert >= BASE:
    result += get_hex_value(number_to_convert % BASE)
    number_to_convert //= BASE

result += get_hex_value(number_to_convert)
print(result[::-1])