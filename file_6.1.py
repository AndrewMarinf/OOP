# Попробуйте создать свой первый dataclass
# Это будет простой класс Point, который должен хранить два целых атрибута x и y .
# На основании класса Point создайте
#  точку с координатами (5, 7) и сохраните ее в  переменную point1
# точку с координатами (-10, 12) и сохраните ее в  переменную point2
# Выведите сперва point1 потом на отдельной строке point2

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point1 = Point(5, 7)
point2 = Point(-10, 12)

print(point1)
print(point2)



# Создайте датакласс  Location

# В нем должны быть описаны следующие атрибуты

# name - обязательный, тип строка
# longitude - необязательный, вещественный тип, значение по умолчанию 0
# latitude - необязательный, вещественный тип, значение по умолчанию 11.5
# Создайте ЭК Location со значениями name='Stonehenge', longitude=51, latitude=1.5  и сохраните его в переменную stonehenge 


from dataclasses import dataclass

@dataclass
class Location:
    name: str
    longitude: int = 0
    latitude: int = 11.5

stronehenge = Location( name='Stonehenge', longitude=51, latitude=1.5)


class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True
    
    

#  1 варик   
text = ['age', 'date', 'address']
for i in text:
    p = hasattr(Person,i)
    if p == True:
        print(f'{i}- YES')
    elif p== False:
        print(f'{i}- NO')    

# 2 варик
for i in input().split():
    if hasattr(Person, i.lower()): # проверка атрибутов в классе Person что они есть или нет с помощью hasattr
        print(i, 'YES', sep='-')
    else:
        print(i, 'NO', sep='-')


    