"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
"""
from decimal import Decimal

MIN_SUM = Decimal(50)
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = Decimal(30)
MAX_COMISSION = Decimal(600)
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = Decimal(5_000_000)
TAX_RATE = Decimal(0.1)

bank_account = Decimal(0)
count = 0
operations = []

def menu(is_flag: bool):
    global count, operations, bank_account
    dct = {'1': 'пополнить счет',
           '2': 'снять со счета',
           '3': 'выйти из программы'}

    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    if bank_account > LIMIT_BEFORE_TAX:
        bank_account *= (1 - TAX_RATE)

    choice = input('Введите команду: ')
    if choice == '3':
        is_flag = False
    elif choice == '1':
        give_money()
        count += 1
    elif choice == '2':
        get_money()
        count += 1
    else:
        print('Неверная команда')
    if count % 3 == 0:
        count = 0
        bank_account *= (1 + BONUS)
        operations.append(f'Начисление бонуса, остаток на счете {bank_account:.2f}')
        print(operations[-1])
    return is_flag


def get_money():
    global operations, bank_account
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= bank_account:
            bank_account = bank_account - (money_to_get + procent)
            operations.append(f'Снятие наличных {money_to_get}, остаток на счете {bank_account:.2f}')
            print(operations[-1])
        else:
            operations.append(f'Ошибка снятие наличных {money_to_get}, недостаточно средств для снятия, '
                              f'остаток на счете {bank_account}')
            print(operations[-1])

    else:
        operations.append(f'Ошибка снятие наличных сумма должна быть кратна {MIN_SUM}, '
                          f'остаток на счете {bank_account:.2f}')
        print(operations[-1])


def give_money():
    global bank_account, operations
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        bank_account += + money_to_give
        operations.append(f'Пополнение счета на сумму {money_to_give}, остаток на счете {bank_account:.2f}')
        print(operations[-1])
    else:
        operations.append(f'Ошибка пополнения счета, сумма должна быть кратна {MIN_SUM}, '
                          f'остаток на счете {bank_account:.2f}')
        print(operations[-1])


if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат')
    is_flag = True
    while is_flag:
        is_flag = menu(is_flag)

    for operation in operations:
        print(operation)
