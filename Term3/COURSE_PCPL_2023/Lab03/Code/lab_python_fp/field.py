""" Задача №1 """


# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


def field(items, *args):
    """

    :param items: список словарей
    :param args: неограниченное количество аргументов

    :returns кортеж или список словарей
    """
    assert len(args) > 0, 'Не передано ни одного аргумента в "args"!'
    if len(args) == 1:
        return (item[item_key] for item in items for item_key in item if
                item[item_key] is not None and item_key == args[0])
    else:
        ans = []
        for item in items:
            tmp = {}
            for arg in args:
                if not item[arg] is None: tmp[arg] = item[arg]
            if tmp: ans.append(tmp)
        return tuple(ans)


def mainTask1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print(*[el for el in field(goods, 'title')], sep=', ')
    print(*field(goods, 'title', 'price'), sep=', ')


if __name__ == '__main__':
    mainTask1()
