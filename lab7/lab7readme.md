#Лабораторная работа 7 - Работа с классами ч. 3
##Задание:
>1.	Создайте класс Employee с общими атрибутами, такими как name (имя), id (идентификационный номер) и методами, например, get_info(), который возвращает базовую информацию о сотруднике.
>2.	Создайте класс Manager с дополнительными атрибутами, такими как department (отдел) и методами, например, manage_project(), символизирующим управление проектами.
>3.	Создайте класс Technician с уникальными атрибутами, такими как specialization (специализация), и методами, например, perform_maintenance(), означающим выполнение технического обслуживания.
>4.	Создайте класс TechManager, который наследует как Manager, так и Technician. Этот класс должен комбинировать управленческие способности и технические навыки, например, иметь методы для управления проектами и выполнения технического обслуживания.
>5.	Добавьте метод add_employee(), который позволяет TechManager добавлять сотрудников в список подчинённых.
>6.	Реализуйте метод get_team_info(), который выводит информацию о всех подчинённых сотрудниках.
> 7.	Создайте объекты каждого класса и демонстрируйте их функциональность.
```python
class Employee:
    name : str
    id_number : str


    id_list = []

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

        if id_number in self.id_list:
            raise ValueError(f'Employee: ID is already taken by another employee')

        self.id_list.append(id_number)

    def get_info(self):
        return f'{self.name}, id{self.id_number}'


class Manager(Employee):
    department : str

    def __init__(self, name, id_number, department):
        Employee.__init__(self, name, id_number)
        self.department = department

    def manage_project(self):
        print(f'project is under management of {self.get_info()}, {self.department}')

class Technician(Employee):
    specialization : str

    def __init__(self, name, id_number, specialization):
        print("fsdf")
        Employee.__init__(self, name, id_number)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f'service is under maintenance of {self.get_info()}, {self.specialization}')

class TechManager(Manager, Technician):
    team_members : list[Employee]

    def __init__(self, name, id_number, department, specialization):
        Manager.__init__(self, name, id_number, department)
        self.specialization = specialization
        self.team_members = []

    def add_employee(self, new_member:Employee) -> None:
        self.team_members.append(new_member)


    def get_team_info(self) -> str:
        return f"{self.name} team: {[member.get_info() for member in self.team_members]}"



if __name__ == "__main__":
    employee1 = Employee("John Smith", "0000")
    employee2 = Employee("Claire Redfield", "0001")
    manager1 = Manager("Jill Valentine", "0002", "STARS")
    manager2 = Manager("Leon Kennedy", "0003", "RCPD")
    technician = Technician("Annette Birkin", "0004", "Biological warfare")
    techmanager1 = TechManager("Albert Wesker", "0005", "Umbrella Corporation", "Biological Warfare")
    techmanager2 = TechManager("Cris Redfield", "0006", "BSAA", "Anti-Biological Warfare")

    techmanager1.add_employee(employee1)
    techmanager1.add_employee(technician)

    techmanager2.add_employee(employee2)
    techmanager2.add_employee(manager2)
    techmanager2.add_employee(manager1)

    employee2.get_info()
    manager1.manage_project()
    technician.perform_maintenance()

    techmanager1.perform_maintenance()
    techmanager1.manage_project()

    print(techmanager1.get_team_info())
    print(techmanager2.get_team_info())
```
В данной программе обратим внимание на следующие моменты. Во-первых, мы используем статический список всех id, чтобы поддерживать их уникальность. 
При попытке добавить сотрудника с уже существующим id вызываем исключение и сообщаем об ошибке.   
Во-вторых, здесь имеет место множественное наследование. При работе с ним возникают сложности, связанные с _Method Resolution Order_. В данном 
случае это будет связано с вызовом родительского конструктора, т.к. при использовании стандартного метода `super()` будет вызван конкструктор сперва одного,
а затем другого родительского класса, что приведет к ошибке. Есть несколько способов решить данную проблему.  
1. Напрямую указать конструктор какого класса вызывается. Данный способ наиболее простой, но при сложной архитектуре проекта код становится плохо
поддерживаемым. Ввиду простоты нашей задачи воспользуемся именно этим способом.
2. Использовать метод `super()` и конструкторы с дополнительными аргументами `args` и `kwargs`.
3. Создать дополнительный родительский ("абстрактный") класс, обозначающий объекты, с которыми мы работаем. Это позволит использовать метод `super()`
с указанием конкретного родительского класса.  
