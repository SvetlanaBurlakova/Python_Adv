"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной
 s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
def variables_without(variables: dict) -> dict:
    lst = {}
    for key, value in variables.items():
        if key != 's' and key.endswith('s'):
            lst[key[:-1]] = value
            globals()[key] = None
    for k,v in lst.items():
        globals()[k] = v


if __name__ == '__main__':
    indexes = [1,2]
    numbers = [1,2,3,4,5,6,7,8,9]
    s = 'stroka'
    number = 6.4
    variables_without(globals())
