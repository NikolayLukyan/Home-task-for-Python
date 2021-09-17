class Employee:
    def __init__(self, name, surname, position, money, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._salary = {'income': money, 'bonus': bonus}


class Position(Employee):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_full_salary(self):
        return f'{sum(self._salary.values())}'


commercial_director = Position('Georg', 'Smith', 'CFO', 500000, 78000)
print(commercial_director.get_full_name())
print(commercial_director.position)
print(commercial_director.get_full_salary())
