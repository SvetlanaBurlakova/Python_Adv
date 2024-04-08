"""
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
"""
from collections import Counter

lst = [1, 2, 3, 1, 2, 3, 1, 8, 7]

dct = {}
dct2 = Counter(lst)

for el in lst:
    dct[el] = dct.get(el, 0) + 1

for k, v in dct.items():
    if v == 2:
        lst.remove(k)
        lst.remove(k)

print(lst)
print(dct)
print(dct2)


