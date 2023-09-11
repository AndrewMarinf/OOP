#    Создайте класс Dog, у которого есть:
# метод __init__, принимающий имя и возраст собаки и сохраняющий их в аргументы name и age
# метод description, который возвращает строку в виде «{name} is {age} years old»
# метод speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}»


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def description(self):
        return (f'{self.name} is {self.age} years old')
    
    def speak (self,sound):
        self.sound = sound
        return (f'{self.name} says {self.sound}')
    
# Ниже код для проверки класса Dog
curt = Dog("Curt", 4)
assert isinstance(curt, Dog)
assert curt.name == 'Curt'
assert curt.age == 4
assert curt.description() == 'Curt is 4 years old'
assert curt.speak("Wo") == 'Curt says Wo'
assert curt.speak("Bow") == 'Curt says Bow'

jack = Dog("Jack", 12)
assert isinstance(curt, Dog)
assert jack.name == 'Jack'
assert jack.age == 12
assert jack.description() == 'Jack is 12 years old'
assert jack.speak("Woof Woof") == 'Jack says Woof Woof'
assert jack.speak("Bow Wow") == 'Jack says Bow Wow'

assert Dog('Karl', 6).description() == 'Karl is 6 years old'        
print('Good')


# Создайте класс Rectangle, который имеет следующие методы:
# метод __init__, который устанавливает значения атрибутов width и height 
# метод area, который возвращает площадь прямоугольника 
# метод perimeter , который возвращает периметр прямоугольника

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
        
# Ниже код для проверки методов класса Rectangle
r1 = Rectangle(2, 3)
assert r1.width == 2
assert r1.height == 3
assert r1.perimeter() == 10
assert r1.area() == 6

r2 = Rectangle(10, 0.5)
assert r2.width == 10
assert r2.height == 0.5
assert r2.perimeter() == 21.0
assert r2.area() == 5.0
print('Good')