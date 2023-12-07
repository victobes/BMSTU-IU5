import unittest
from main import *


# Тестирование класса "Компьютер"
class TestComputer(unittest.TestCase):

    def test_computer_creation(self):
        computer = Computer(1, "Lenovo", 2022, 1)
        self.assertEqual(computer.id, 1)
        self.assertEqual(computer.manufacturer_name, "Lenovo")
        self.assertEqual(computer.manufacture_year, 2022)
        self.assertEqual(computer.class_id, 1)


# Тестирование класса "Дисплейный класс"
class TestComputerClassroom(unittest.TestCase):

    def test_computer_classroom_creation(self):
        computer_classroom = ComputerClassroom(1, "254л")
        self.assertEqual(computer_classroom.id, 1)
        self.assertEqual(computer_classroom.number, "254л")


# Тестирование класса для реаизации связи многие-ко-многим "Компютеры класса"
class TestClassroomsComputers(unittest.TestCase):

    def test_classrooms_computers_creation(self):
        classrooms_computers = ClassroomsComputers(1, 1)
        self.assertEqual(classrooms_computers.computer_id, 1)
        self.assertEqual(classrooms_computers.classroom_id, 1)


#
class TestTaskExecution(unittest.TestCase):
    def setUp(self):
        self.computer_classrooms, self.computers, self.classrooms_computers = generate_data()

    # Тестирование запроса №1
    def test_task1(self):
        result = task1(self.computer_classrooms, self.computers)
        self.assertEqual(result, [("Acer", "253л"), ("Acer", "306э"), ("Asus", "362"), ("Apple", "107л")])

    # Тестирование запроса №2
    def test_task2(self):
        result = task2(self.computer_classrooms, self.computers)
        self.assertEqual(result, [("362", 2017), ("253л", 2019), ("254л", 2020), ("306э", 2020), ("107л", 2020)])

    # Тестирование запроса №3
    def test_task3(self):
        result = task3(self.computer_classrooms, self.computers, self.classrooms_computers)
        self.assertEqual(result,
                         [("Acer", "253л"), ("Acer", "306э"), ("Apple", "107л"), ("Asus", "362"), ("Lenovo", "254л"),
                          ("Lenovo", "254л"), ("Lenovo", "306э")])


if __name__ == "__main__":
    unittest.main()
