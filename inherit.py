class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working and his age is {self.age}..............")


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def per(self):
        print(f'{self.level} level is {self.name}')


class Designer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def per(self):
        print(f'{self.level} level is {self.name}')


se = SoftwareEngineer("Max", 25, 27000, "Experience")
se.work()
se.per()

d = Designer("Philips", 27, 25000, "Junior")
d.work()
d.per()


# this is Polymarphism from the list of the classes
employees = [SoftwareEngineer("Max", 25, 27000, "Experience"),
             Designer("Philips", 27, 25000, "Junior")]


def motivate_employees(employees):
    for employee in employees:
        employee.per()


motivate_employees(employees)
