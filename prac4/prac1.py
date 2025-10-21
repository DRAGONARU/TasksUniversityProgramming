class Employee():
    '''
    Родительский класс для работников
    Поля:
        name - имя работника
        salary - зарплата работника
    '''
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        '''
        Возвращает зарплату работника
        '''
        return self.salary

class Manager(Employee):
    '''
    Класс для менеджеров, дочерний от родительского класса Employee
    Поля:
        name - имя менеджера
        salary - зарплата менеджера
        developers_optimized - количество оптимизированных разработчиков

    '''
    def __init__(self, name, salary, developers_optimized):
        Employee.__init__(self, name, salary)
        self.developers_optimized = developers_optimized
    
    def optimize_developers(self):
        '''
        Метод для оптимизации разработчиков
        '''
        self.developers_optimized += 1

    def get_salary(self):
        '''
        Метод для получения зарплаты менеджера
        '''
        return (self.salary + self.developers_optimized * 1000)

class Developer(Employee):
    '''
    Класс для разработчиков, дочерний от родительского класса Employee
    Поля:
        name - имя разработчика
        salary - зарплата разработчика
        coffe_consumed - количество выпитого кофе
        beer_consumed - количество выпитого пива
    '''
    def __init__(self, name, salary, coffe_consumed, beer_consumed):
        Employee.__init__(self, name, salary)
        self.coffe_consumed = coffe_consumed
        self.beer_consumed = beer_consumed
    
    def consume_coffee(self):
        '''
        Метод для потребления кофе
        '''
        self.coffe_consumed += 1
    
    def consume_beer(self):
        '''
        Метод для потребления пива
        '''
        self.beer_consumed += 1

    def get_salary(self):
        '''
        Метод для получения зарплаты разработчика
        '''
        return (self.salary + self.coffe_consumed * 100 - self.beer_consumed * 150)
    
developer_1 = Developer('Дмитрий', 100000, 5, 3)
manager_1 = Manager('Иван', 50000, 2)
print(developer_1.get_salary())
print(manager_1.get_salary())
developer_1.consume_coffee()
developer_1.consume_beer()
print(developer_1.get_salary())
manager_1.optimize_developers()
print(manager_1.get_salary())
