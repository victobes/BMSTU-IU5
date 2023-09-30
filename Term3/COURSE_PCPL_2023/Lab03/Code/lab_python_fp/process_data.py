import json

# Сделаем другие необходимые импорты
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.gen_random import gen_random

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария
path = "/Users/victoria/PycharmProjects/lab03/data_light.json"

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    """
    Выводит отсортированный список профессий без повторений.
    Регистр игнорируется при сортировке.
    :param arg: json-файл
    :return: отсортированный список
    """
    return sorted(list(set([item['job-name'].capitalize() for item in arg])))


@print_result
def f2(arg):
    """
    Фильтрует входной массив и возвращает только те элементы, которые начинаются со слова "программист"
    :param arg: список
    :return: отфильтрованный список
    """
    return list(filter(lambda text: (text.split())[0] == 'Программист', arg))


@print_result
def f3(arg):
    """
    Модифицирует каждый элемент списка посредством добавления к нему строки “с опытом Python”
    :param arg: список
    :return: модифицированный список
    """
    return list(map(lambda text: text + ' с опытом Python', arg))


@print_result
def f4(arg):
    """
    Генерирует для каждой специальности зарплату от 100 000 до 200 000 рублей и присоединяет её к названию специальности.
    Пример: "Программист C# с опытом Python, зарплата 137287 руб"
    :param arg: список
    :return:список
    """
    tmp = list(zip(arg, [', зарплата ' + str(salary) + ' руб.' for salary in gen_random(len(arg), 100000, 200000)]))
    return [item[0] + item[1] for item in tmp]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
