""" Задача 3 """

# Нужно реализовать конструктор
# В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
# в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
# Например: ignore_case = True, Aбв и АБВ - разные строки
#           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
# По-умолчанию ignore_case = False
from lab_python_fp.gen_random import gen_random


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self._used_data = set()
        self._data = items
        self._index = 0

        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):

        # Если bool-параметр ignore_case(игнорирование регистра) истинен,
        # то все элементы приводяся к нижнему регистру
        if self.ignore_case:
            for counter, el in enumerate(self._data):
                if type(el) is str:
                    self._data[counter] = el.lower()

        while True:
            if self._index >= len(self._data):
                raise StopIteration
            else:
                current = self._data[self._index]
                self._index += 1
                if current not in self._used_data:
                    self._used_data.add(current)
                    return current

    def __iter__(self):
        return self


def mainTask3():
    print('__________ТЕСТ 1__________')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item)

    print('__________ТЕСТ 2__________')
    data = gen_random(10, 1, 3)
    for item in Unique(data):
        print(item)

    print('__________ТЕСТ 3__________')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Случай 1: без ignore_case')
    for item in Unique(data):
        print(item)

    print('Случай 2: ignore_case=True')
    for item in Unique(data, ignore_case=True):
        print(item)


if __name__ == '__main__':
    mainTask3()
