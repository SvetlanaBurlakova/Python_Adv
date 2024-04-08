"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы: Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует Для решения используйте операции
с множествами. Код должен расширяться на любое большее количество друзей
"""

dct = {'Саша': ('рюкзак', 'спички', 'бутылка', 'фляжка'),
       'Паша': ('рюкзак', 'котелок', 'бутылка'),
       'Даша': ('рюкзак', 'спички', 'палатка')}

all = set()
two = set()
one = set()

for k, v in dct.items():
    if all:
        all = all.intersection(set(v))
    else:
        all.update(set(v))

print(all, 'у всех есть')

dic_count = {}
for k, v in dct.items():
    for value in v:
        dic_count[value] = dic_count.get(value, 0) + 1
friends = len(list(dct.keys())) - 1
things = []
for k, v in dic_count.items():
    if v == friends:
        things.append(k)
for k, v in dct.items():
    for item in things:
        if item not in v:
            print(f"{item} нет у {k}!")
            break
one_thing = []
for k, v in dic_count.items():
    if v == 1:
        one_thing.append(k)
print("Вещи в единственном экземпляре: ", *one_thing)
