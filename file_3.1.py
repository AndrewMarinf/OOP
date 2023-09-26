
class Person:
    def __init__(self,name,surname,gender = 'male') -> str:
        self.name = name
        self.surname = surname
        self.gender = gender
    
        if self.gender == "female" or self.gender == 'male':
            self.gender = gender

        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = gender
    
    def __str__(self):
        if self.gender == 'male':
            return (f"Гражданин {self.surname} {self.name}")
        else:
            return (f"Гражданка {self.surname} {self.name}")


# Ниже код для проверки методов класса Person
p1 = Person('Chuck', 'Norris')
assert p1.name == 'Chuck'
assert p1.surname == 'Norris'
assert p1.gender == 'male'
assert isinstance(p1, Person)
assert str(p1) == 'Гражданин Norris Chuck'

p2 = Person('Оби-Ван', 'Кеноби', True) #  нужно распечатать предупреждение из условия
assert str(p2) == 'Гражданин Кеноби Оби-Ван'
assert p2.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'gender': 'male'}
assert isinstance(p2, Person)

p3 = Person('Mila', 'Kunis', 'female')
assert isinstance(p3, Person)
assert str(p3) == 'Гражданка Kunis Mila'

print(p1)
print(p2)
print(p3)


# Создайте класс Person, у которого есть: 

# конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
 
# переопределить метод __str__ следующим образом: 
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>"
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>"

# СОЗДАТЬ БЕЗ SETTOR!!!

class Person:

    def __init__(self, name, surname, gender = 'male'):
        self.name = name
        self.surname = surname
        self.gender = gender
        
        if gender in ("male", "female"):
            self.gender = gender
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"

    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        if self.gender == 'female':
            return f"Гражданка {self.surname} {self.name}"

            
# Ниже код для проверки методов класса Person
p1 = Person('Chuck', 'Norris')
assert p1.name == 'Chuck'
assert p1.surname == 'Norris'
assert p1.gender == 'male'
assert isinstance(p1, Person)
assert str(p1) == 'Гражданин Norris Chuck'

p2 = Person('Оби-Ван', 'Кеноби', True) #  нужно распечатать предупреждение из условия
assert str(p2) == 'Гражданин Кеноби Оби-Ван'
assert p2.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'gender': 'male'}
assert isinstance(p2, Person)

p3 = Person('Mila', 'Kunis', 'female')
assert isinstance(p3, Person)
assert str(p3) == 'Гражданка Kunis Mila'

print(p1)
print(p2)
print(p3)


# Давайте определим магические методы __str__ и __repr__ для класса GroceryItem, представляющего продуктовый товар:

# Создайте класс GroceryItem, который имеет следующие методы:

# метод __init__, который устанавливает значения атрибутов name, price и quantity: название товара, его цену и количество
 
# магический метод __str__, который возвращает строковое представление товара в следующем виде:
# Name: {name}
# Price: {price}
# Quantity: {quantity}

# магический метод __repr__, который возвращает однозначное строковое представление объекта
# GroceryItem({name}, {price}, {quantity})

class GroceryItem:
    
    def __init__(self,name,price,quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'
    
    def __repr__(self) -> str:
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'
    
# Ниже код для проверки методов класса GroceryItem
banana = GroceryItem('Banana', 10, 5)
assert banana.__str__() == """Name: Banana
Price: 10
Quantity: 5"""
assert repr(banana) == 'GroceryItem(Banana, 10, 5)'
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
assert dragon_fruit.__str__() == """Name: Dragon fruit
Price: 5
Quantity: 350"""
assert repr(dragon_fruit) == 'GroceryItem(Dragon fruit, 5, 350)'
print(dragon_fruit)
print(f"{dragon_fruit!r}")    
    

