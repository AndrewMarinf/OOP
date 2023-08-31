#Ниже определен класс Book. Наша задача вывести на разных строках сначала атрибут класса writer, а затем атрибут name

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

print(Book.writer)
print(Book.name)

# Перед нами все тот же класс Book, но теперь ваша задача получить доступ к атрибутам writer и pages при помощи функции getattr
# Сперва выведите атрибут writer, затем на новой строке pages

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    
print(getattr(Book,"writer"))
print(getattr(Book,"pages"))

# Теперь ваша задача изменить значения атрибутов name и pages:

# в атрибут name необходимо присвоить значение «Скотный двор»
# в атрибут pages необходимо положить значение 115
# Изменение атрибутов необходимо выполнить при помощи функции setattr

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213


setattr(Book,"name",'Скотный двор')
setattr(Book,"pages",115)


# Давайте теперь добавим в класс Book два новых атрибута:

# атрибут rating со значением 8.7;
# атрибут genre со значением «dystopian»;
# Создайте один атрибут обязательно через функцию setattr, второй  через присвоение

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

Book.rating = 8.7
setattr(Book,'genre','dystopian')


# Теперь давайте тренироваться удалять атрибуты в классе. Для этого вам необходимо из класса Book удалить три атрибута:

# pages 
# writer
# rating
# Удаление выполните с помощью оператора del и функции delattr

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    rating = 8.7
    genre = 'dystopian'
    
del Book.pages
del Book.writer 
delattr(Book,'rating')

# Вам необходимо создать класс Cat и внутри него два атрибута класса:
# атрибут name со значением 'Матроскин'
# атрибут color со значением 'black'
# После этого создайте экземпляр класса и сохраните его в переменную my_cat

class Cat:
    name = 'Матроскин'
    color = 'black'
    
my_cat = Cat()

# Почему иногда для создания атрибута лучше использовать функцию setattr может продемонстрировать эта задача.
# Имеется пустой класс Empty и список кортежей my_list.
# Ваша задача — взять каждый первый элемент кортежа и создать на его основе название атрибута в классе Empty , а в качестве значения присвоить второй элемент кортежа.
# В итоге в классе Empty  должно появиться десять новых атрибутов.

class Empty:
    pass       

my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]

for i in my_list:
    setattr(Empty,i[0],i[1])


# Ниже определен пустой класс SuperHero. Ваша задача  создать два ЭК и сохранить их в переменные batman и superman
# Для ЭК, хранящегося в переменной batman, необходимо создать
# атрибут can_fly со значением False
# атрибут damage со значением 175
# Для ЭК, хранящегося в переменной superman, необходимо создать
# атрибут can_fly со значением True
# атрибут damage со значением 285
# атрибут alter_ego со значением 'Кларк Кент'

class SuperHero:
    pass

class SuperHero:
    pass

batman = SuperHero()
batman.can_fly = False
batman.damage = 175

superman = SuperHero()
superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'

# Имеется пустой класс Config. Ваша задача написать функцию create_instance, которая принимает на вход положительное число N. Функция должна создать ЭК , создать у него N атрибутов и вернуть в качестве ответа полученный ЭК.
# Что касается атрибутов, они должны называться определенным образом и иметь определенное значение. В общем виде это можно записать так
# attribute<n> = "value<n>"
# где n — порядковый номер атрибута. Значение атрибута - строковый тип
class Config:     
    pass
def create_instance(n: int) -> Config:
    obj = Config() # объявление экземпляра класса
    for i in range(1,n+1):
        setattr(obj, f'attribute{i}', f'value{i}') # создание нового атрибута
    return obj