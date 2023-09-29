from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pandas as pd
import cowsay

def main():
    r = Rectangle("синего", 4, 4)
    c = Circle("зеленого", 4)
    s = Square("красного", 4)
    print(r, c, s, sep='\n')

    print("\n__________ТАБЛИЦА ФИГУР___________")
    data = {"Фигура": ["Прямоугольник", "Круг", "Квадрат"], "Цвет": ["Синий", "Зеленый", "Красный"],
            "Площадь": [16, 50.27, 16]}
    table = pd.DataFrame(data, )
    print(table, '\n')

    print(cowsay.turkey("Лабораторная работа №2"))

if __name__ == "__main__":
    main()
