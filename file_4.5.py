
# class Person:
#     def __init__(self,name,passport) -> str:
#         self.name = name
#         self.passport = passport

#     def display(self):
#         print(f'{self.name}: {self.passport}')  

# class Employee(Person):
#     def __init__(self, name, passport,salary,department) -> str:
#         super().__init__(name, passport)
#         self.salary = salary
#         self.department = department

# assert issubclass(Employee, Person)

# emp = Person("just human", 123456)
# emp.display()
# assert emp.__dict__ == {'name': 'just human', 'passport': 123456}

# emp2 = Employee("Geek2", 534432, 321321, 'Roga & Koputa')
# emp2.display()
# assert emp2.__dict__ == {'salary': 321321, 'department': 'Roga & Koputa',
#                          'name': 'Geek2', 'passport': 534432}


# class Vehicle:
#     def __init__(self,name,mileage,capacity) -> float:
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

#     def display(self):
#         print(f'Total {self.name} fare is: {self.fare()}')

# class Bus(Vehicle):
#     def __init__(self, name, mileage, capacity = 50) -> int:
#         super().__init__(name, mileage, capacity)

#     def fare(self):
#         return super().fare() / 100 * 10 + super().fare() # увеличилось на 10% можно и число Х * 10 / 100 будет 10%

# class Taxi(Vehicle):
#     def __init__(self, name, mileage, capacity = 4) -> int:
#         super().__init__(name, mileage, capacity)

#     def fare(self):
#         return super().fare() / 100 * 35 + super().fare()    # увеличилсоь на 35%


# class Taxi(Vehicle):
#     def __init__(self, name, mileage, capacity = 4) -> int:
#         super().__init__(name, mileage, capacity)

#     def face(self):
#         return super().face() / 100 * 35 + super().fare()    # увеличилсоь на 35%




class Transport:
    def __init__(self,brand,max_speed,kind = None) -> None:
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind 

    def __str__(self) -> str:
        return f"Тип транспорта {self.kind} марки {self.brand } может развить скорость {self.max_speed} км/ч"  

class Car(Transport):
    def __init__(self, brand, max_speed, mileage , __gasoline_residue,) -> None:
        super().__init__(brand, max_speed, kind = 'Car',)
        self.__gasoline_residue = __gasoline_residue
        self.mileage = mileage

    @property
    def gasoline(self):
        return f"Осталось бензина {self.__gasoline_residue} л"
    
    @gasoline.setter
    def gasoline(self,value):
        if  isinstance(value,int):
            self.__gasoline_residue += value 
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')   
    
class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name) -> None:
        super().__init__(brand, max_speed, kind = 'Boat')
        self.owners_name = owners_name

    def __str__(self) -> str:
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}' 

class Plane(Transport):
    def __init__(self, brand, max_speed,capacity) -> None:
        super().__init__(brand, max_speed, kind = 'Plane')
        self.capacity = capacity

    def __str__(self) -> str:
        return  f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'   



# Ниже располагается код для проверки

p1 = Transport('Chuck', 50)
print(p1)
assert isinstance(p1, Transport)
assert p1.kind == None
assert p1.brand == 'Chuck'
assert p1.max_speed == 50
assert p1.__dict__ == {'kind': None, 'brand': 'Chuck', 'max_speed': 50}

c1 = Car('RRR', 50, 150, 999)
print(c1)

assert isinstance(c1, Car)
assert c1.kind == "Car"
assert c1.brand == 'RRR'
assert c1.max_speed == 50
assert c1.mileage == 150
assert c1.gasoline == 'Осталось бензина 999 л'
c1.gasoline = 100
assert c1.gasoline == 'Осталось бензина 1099 л'
assert c1.__dict__ == {'kind': 'Car', 'brand': 'RRR', 'max_speed': 50,
                       'mileage': 150, '_Car__gasoline_residue': 1099}

b1 = Boat('XXX', 1150, 'Arkasha')
print(b1)
assert isinstance(b1, Boat)
assert b1.kind == "Boat"
assert b1.brand == 'XXX'
assert b1.max_speed == 1150
assert b1.owners_name == 'Arkasha'

pla = Plane('www', 2150, 777)
print(pla)
assert isinstance(pla, Plane)
assert pla.kind == "Plane"
assert pla.brand == 'www'
assert pla.max_speed == 2150
assert pla.capacity == 777

transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Автомобиль успешно заправлен'
print(first_car.gasoline)  # Осталось бензина на 350 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr