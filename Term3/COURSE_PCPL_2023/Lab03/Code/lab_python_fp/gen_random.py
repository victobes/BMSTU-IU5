""" Задача 2 """
from random import randint


# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки

def gen_random(num_count, begin, end):
    """
    Генерация случайных чисел

    :param num_count: количество случайных чисел
    :param begin: минимальное число
    :param end: максимальное число
    :return: кортеж случайных чисео
    """
    return [randint(begin, end) for _ in range(num_count)]


def mainTask2():
    print(*gen_random(5, 1, 3), sep=', ')


if __name__ == '__main__':
    mainTask2()
