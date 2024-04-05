"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""
from fractions import Fraction
from math import gcd

def check_gcd(num1: int, num2: int):
    return str(int(num1 / gcd(num1, num2))), str(int(num2 / gcd(num1, num2)))


frac_1 = input('Введите первую дробь в формате a/b: ')
frac_2 = input('Введите вторую дробь в формате a/b: ')

num_of_frac_1, den_of_frac_1 = frac_1.split('/')
num_of_frac_1, den_of_frac_1 = int(num_of_frac_1), int(den_of_frac_1)
num_of_frac_2, den_of_frac_2 = frac_2.split('/')
num_of_frac_2, den_of_frac_2 = int(num_of_frac_2), int(den_of_frac_2)

sum_of_frac_num = num_of_frac_1 * den_of_frac_2 + num_of_frac_2 * den_of_frac_1
frac_den = den_of_frac_1 * den_of_frac_2
mult_of_frac_num = num_of_frac_1 * num_of_frac_2

sum_of_frac_num, frac_den_sum = check_gcd(sum_of_frac_num, frac_den)
mult_of_frac_num, frac_den_mult = check_gcd(mult_of_frac_num, frac_den)

if sum_of_frac_num == frac_den_sum:
    print(f'{frac_1} + {frac_2} = 1')
else:
    print(f'{frac_1} + {frac_2} = {sum_of_frac_num}/{frac_den_sum}')

print(f'Проверка суммы: {Fraction(frac_1) + Fraction(frac_2)}')

if mult_of_frac_num == frac_den_mult:
    print(f'{frac_1} * {frac_2} = 1')
else:
    print(f'{frac_1} * {frac_2} = {mult_of_frac_num}/{frac_den_mult}')

print(f'Проверка произведения: {Fraction(frac_1) * Fraction(frac_2)}')

