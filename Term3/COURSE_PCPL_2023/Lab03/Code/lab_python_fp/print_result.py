""" Задача 5"""


# Реализация декоратора
def print_result(func):
    def wrapper(*args, **kwargs):
        # фактические и формальные парамтеры опциональны в данном случае
        print(func.__name__)
        original_result = func(*args, **kwargs)
        if isinstance(original_result, list):
            for _ in original_result:
                print(_)
            return original_result
        elif isinstance(original_result, dict):
            for key, value in original_result.items():
                print('{} = {}'.format(key, value))
            return original_result
        else:
            print(original_result)
            return original_result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def mainTask5():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    mainTask5()
