"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
"""
for k in range(0, 5, 4):
    for j in range(2, 11):
        for i in range(2, 6):
            print(f'{i + k} * {j} = {(i + k) * j}',end='\t\t')
        print()
    print()
