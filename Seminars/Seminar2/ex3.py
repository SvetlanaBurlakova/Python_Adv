"""
Двоичное и восьмиричное представление
"""
BASE = 8

number = int(input('Введите число: '))
print(oct(number))
result = ''
while number > BASE:
    result += str(number % BASE)
    number //= BASE
result += str(number)
print(result[::-1])
