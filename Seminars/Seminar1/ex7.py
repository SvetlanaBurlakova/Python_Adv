"""
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число Откажитесь от магических чисел
В коде должны быть один input и один print
"""
while True:
    num = int(input('Введите число: '))
    if 1 < num < 999:
        break

if num < 10:
    print(num ** 2)
elif num < 100:
    print((num % 10) * (num // 10))
else:
    print((num % 10) * 100 + (num // 100) + (num // 10 % 10) * 10)

