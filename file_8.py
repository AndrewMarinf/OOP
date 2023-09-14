# Создайте класс Rectangle, у которого есть:
# конструктор __init__, принимающий 2 аргумента: длину и ширину. 
# свойство area, которое возвращает площадь прямоугольника;
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
# print(r1.area) # 15
# print(r2.area) # 6

class Rectangle:

    def __init__(self,x,y) -> int:
        self.x = x
        self.y = y

    @property
    def aref(self):
            self.aref = self.x * self.y
        # return  self.aref   # почему то выдает ошибку

# Ниже код для проверки методов класса Rectangle


r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976        
print('Good')




class Square:
    def __init__(self, s):
        self.__side = s
        self.__perimetr = None

    @property
    def perimetr(self):
        if self.__perimetr is None:
            print('calculating perimetr')
            self.__perimetr = self.side * 4
        return self.__perimetr

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__perimetr = None