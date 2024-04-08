"""
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа
"""
tpl = (1, 3.14, 'Hello', [1, 2, 3], 4, 5.6, 'Hi')

dct = {}
for element in tpl:
    if type(element).__name__ not in dct:
        dct[type(element).__name__] = [element]
    else:
        dct[type(element).__name__].append(element)

print(dct)