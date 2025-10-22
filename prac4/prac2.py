class vehicle():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class car(vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    
    def description(self):
        print(f"Это машина, она имеет 4 колеса, маленький размер")

class tank(vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    
    def description(self):
        print(f"Это танк, он передвигается на гусеницах, и он достаточно большой")

class plane(vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    
    def description(self):
        print(f"Это самолет, он летает, у него нет колёс")


car1 = car("Лада", 1000)
tank1 = tank("Т-90М", -24)
plane1 = plane("Рафаль", 30000)
car1.description()
tank1.description()
plane1.description()
