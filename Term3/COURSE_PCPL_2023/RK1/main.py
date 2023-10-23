class Computer:
    """Компьютер"""

    def __init__(self, id: int, manufacturer_name: str, manufacture_year: int, class_id: int):
        self._id = id
        self._manufacturer_name = manufacturer_name
        self._manufacture_year = manufacture_year
        self._class_id = class_id

    @property
    def id(self) -> int:
        return self._id

    @property
    def class_id(self) -> int:
        return self._class_id

    @property
    def manufacturer_name(self) -> str:
        return self._manufacturer_name

    @property
    def manufacture_year(self) -> int:
        return self._manufacture_year


class ComputerClassroom:
    """Дисплейный класс"""

    def __init__(self, id: int, number: str):
        self._id = id
        self._number = number

    @property
    def id(self) -> int:
        return self._id

    @property
    def number(self) -> str:
        return self._number


class ClassroomsComputers:
    """
    'Компьютеры класса' для реализации
    связи многие-ко-многим
    """

    def __init__(self, computer_id: int, classroom_id: int):
        self._computer_id = computer_id
        self._classroom_id = classroom_id

    @property
    def computer_id(self) -> int:
        return self._computer_id

    @property
    def classroom_id(self) -> int:
        return self._classroom_id


def task1(computer_classrooms: list[ComputerClassroom], computers: list[Computer]):
    print("Запрос № 1")
    data = [(computer, classroom) for computer in computers for classroom in computer_classrooms if
            computer.class_id == classroom.id and computer.manufacturer_name.startswith("A")]
    for (computer, classroom) in data:
        print(computer.manufacturer_name, classroom.number)
    print()


def task2(computer_classrooms: list[ComputerClassroom], computers: list[Computer]):
    print("Запрос № 2")
    data = {}
    for computer_classroom in computer_classrooms:
        classroom_manufacture_years = [computer.manufacture_year for computer in computers for classroom in
                                       computer_classrooms if
                                       computer.class_id == classroom.id and classroom.id == computer_classroom.id]
        data[computer_classroom.number] = min(classroom_manufacture_years)

    data_items = list(data.items())
    data_items.sort(key=lambda x: x[1])
    for (classroom, earliest_year) in data_items:
        print(classroom, earliest_year)
    print()


def task3(computer_classrooms: list[ComputerClassroom], computers: list[Computer],
          classrooms_computers: list[ClassroomsComputers]):
    print("Запрос № 3")
    data = [(computer, computer_classroom) for cc in classrooms_computers for computer in computers for
            computer_classroom in computer_classrooms if
            cc.computer_id == computer.id and cc.classroom_id == computer_classroom.id]

    data.sort(key=lambda x: x[0].manufacturer_name)

    for (computer, classroom) in data:
        print(computer.manufacturer_name, classroom.number)
    print()


def main():
    """Основная функция"""

    # Дисплейные классы
    computer_classrooms = [
        ComputerClassroom(1, "254л"),
        ComputerClassroom(2, "253л"),
        ComputerClassroom(3, "306э"),
        ComputerClassroom(4, "362"),
        ComputerClassroom(5, "107л")
    ]

    # Компьютеры
    computers = [
        Computer(1, "Lenovo", 2022, 1),
        Computer(2, "Lenovo", 2020, 1),
        Computer(3, "Acer", 2019, 2),
        Computer(4, "Lenovo", 2021, 3),
        Computer(5, "Acer", 2020, 3),
        Computer(6, "Asus", 2017, 4),
        Computer(7, "Apple", 2020, 5)
    ]

    classrooms_computers = [
        ClassroomsComputers(1, 1),
        ClassroomsComputers(2, 1),
        ClassroomsComputers(3, 2),
        ClassroomsComputers(4, 3),
        ClassroomsComputers(5, 3),
        ClassroomsComputers(6, 4),
        ClassroomsComputers(7, 5)
    ]

    task1(computer_classrooms, computers)
    task2(computer_classrooms, computers)
    task3(computer_classrooms, computers, classrooms_computers)


if __name__ == "__main__":
    main()
