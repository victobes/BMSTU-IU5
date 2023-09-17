# Copyright 2023 Victoria Bespalova <vickycat2014@gmail.com>

import sys
import math


def get_coef(index, prompt) -> float:
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        try:
            coef_str = sys.argv[index]
            # Переводим строку в действительное число
            coef = float(coef_str)
            return coef
        except ValueError:
            # Некорректное значение коэффициента, повторяем ввод
            pass
    except:
        # Вводим с клавиатуры
        while True:
            try:
                print(prompt)
                coef_str = input()
                # Переводим строку в действительное число
                coef = float(coef_str)
                return coef
            except ValueError:
                # Некорректное значение коэффициента, повторяем ввод
                pass


def get_quadratic_equation_roots(a, b, c) -> tuple:
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        tuple(float): Кортеж корней
    '''
    result = ()
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result += (root,)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result += (root1, root2)

    return result


def get_biquadratic_equation_roots(a, b, c) -> tuple:
    # Вычисление корней квадратного уравнения
    roots = get_quadratic_equation_roots(a, b, c)
    result = ()
    for root in roots:
        if root > 0.0:
            result += (math.sqrt(root),)
            result += (-1 * math.sqrt(root),)
        elif root == 0.0:
            result += (root,)

    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_biquadratic_equation_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    else:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    print('_________Лабораторная работа №1_________')
    main()
