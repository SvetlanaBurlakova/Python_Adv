"""
Продолжаем развивать задачу 2. Возьмите словарь, который вы получили.
Сохраните его итератор. Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
from sys import getsizeof

text = 'Ехал Грека чрез реку!'
dct = {c: ord(c) for c in text}

text_iter = iter(dct.items())
print(text_iter, type(text_iter), getsizeof(text_iter))

for i in range(5):
    print(next(text_iter))