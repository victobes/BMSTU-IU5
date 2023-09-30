""" Задача 4"""

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


# Сортировка по модулю в порядке убывания
def mainTask4():
    result = sorted(data, key=abs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)


if __name__ == '__main__':
    mainTask4()
