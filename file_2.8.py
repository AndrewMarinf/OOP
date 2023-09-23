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


#   Создайте класс Date, у которого есть:
# конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
# свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
# свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
# print(d1.date) # 05/10/2001
# print(d1.usa_date) # 10-05-2001
# print(d2.date) # 15/03/0999
# print(d2.usa_date) # 03-15-0999
# Обратите внимание, что дни и месяцы занимают 2 символа в выводе, а отображение года- 4 символа(заполняются нулями спереди до нужной длины). 

class Date:
    def __init__(self, day, month, year):
         self.day = day
         self.month = month
         self.year = year


    @property
    def date(self):
        return (f"{self.day:02d}/{self.month:02d}/{self.year:04d}")

    @property
    def usa_date(self):
        return (f"{self.month:02d}-{self.day:02d}-{self.year:04d}")
    
# Ниже код для проверки методов класса Date

d1 = Date(5, 10, 2001)
assert isinstance(d1, Date)
assert d1.date == '05/10/2001'
assert d1.usa_date == '10-05-2001'
assert isinstance(type(d1).date, property), 'Вы не создали property date'
print(d1.date, d1.usa_date)

d2 = Date(15, 3, 999)
assert isinstance(d2, Date)
assert d2.date == '15/03/0999'
assert d2.usa_date == '03-15-0999'
assert isinstance(type(d2).date, property), 'Вы не создали property date'
print(d2.date, d2.usa_date)

d3 = Date(3, 5, 3)
assert d3.date == '03/05/0003'
assert d3.usa_date == '05-03-0003'
print(d3.date, d3.usa_date)