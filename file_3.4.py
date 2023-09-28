# Создайте класс  Fruit, который имеет:

# метод __init__, который устанавливает значения атрибутов name и price: название и цена фрукта
 
# методы сравнения. Здесь вы сами решаете какие магические методы реализовывать, главное чтобы фрукты могли сравниваться с числами и другими фруктами по цене. Смотрите тесты ниже в коде


# ТУТ СОКРАЩЕННЫЙ КОД
from functools import total_ordering
@total_ordering
class Fruit:
    def __init__(self,name,price) -> (str,float):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.price == other.price 
        elif isinstance(other, (int, float)): # чтобы сравнивать с числом вроде 
            return self.price == other
        else:
            False 
            

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return self.price < other.price
        elif isinstance(other, (int, float)):
            return self.price < other
        else:
            False


# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)


assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False
print('good')
assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')

#   ТУТ ВСЕ РАСПИСАНО
class Fruit:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other

    def __ne__(self, other):
        return not self.price == other

    def __lt__(self, other):
        return self.price < other

    def __gt__(self, other):
        return self.price > other

    def __le__(self, other):
        return self.price <= other

    def __ge__(self, other):
        return self.price >= other
    
# код из документации
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, (int, float)):
            return self.age  == other
        else:
            return False
    
john = Person('John', 'Doe', 25)
print(john == 25)


