# Создайте класс Registration, который пока будет проверять только введенный логин. Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

# В классе Registration необходимо реализовать:

# метод __init__ принимающий один аргумент логин пользователя. Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3). То есть когда отработает данный код 
# def __init__(self, логин):
#     self.login = логин # передаем в сеттер login значение логин 
# должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

# Cвойство геттер login, которое возвращает значение self.__login;
 
# Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
# строковое значение, если поступают другие типы данных необходимо вызвать исключение при помощи строки raise TypeError
 
# логин, так как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError
 
# логин должен содержать символ точки «.» после символа «@».В случае, если после @ нету точки, вызываем исключение при помощи строки raise ValueError
# Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login

# class Robot:
#     population = 0

#     def __init__(self,name) -> None:
#         self.name = name
#         print(f'Робот {self.name} был создан')
#         Robot.population+= 1 # тут надо добавлять именно в КЛАСС , а не в ЭК

#     def destroy(self):
#         Robot.population-= 1 # тут надо убирать именно в КЛАСС , а не в ЭК
#         print(f'Робот {self.name} был уничтожен')

#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')    

#     @classmethod
#     def how_many(cls):
#         print(f'{cls.population}, вот сколько нас еще осталось')

# # код ниже не нужно удалять, в нем находятся проверки


# droid1 = Robot("R2-D2")
# assert droid1.name == 'R2-D2'
# assert Robot.population == 1
# droid1.say_hello()
# Robot.how_many()
# droid2 = Robot("C-3PO")
# assert droid2.name == 'C-3PO'
# assert Robot.population == 2
# droid2.say_hello()
# Robot.how_many()
# droid1.destroy()
# assert Robot.population == 1
# droid2.destroy()
# assert Robot.population == 0
# Robot.how_many()



#  Создайте базовый класс User, у которого есть:

# метод __init__, принимающий имя пользователя и его роль. Их необходимо сохранить в атрибуты экземпляра name и role соответственно
# Затем создайте класс Access , у которого есть:

# приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
 
# приватный статик-метод __check_access , который принимает название роли и возвращает True, если роль находится в списке __access_list , иначе - False
 
# публичный статик-метод get_access , который должен принимать экземпляр класса User и проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access  . Если у пользователя достаточно прав, выведите на экран сообщение
# «User <name>: success», если прав недостаточно - «AccessDenied»
# Если передается тип данных, отличный от экземпляр класса User, необходимо вывести сообщение:
# «AccessTypeError»
# user1 = User('batya99', 'admin')
# Access.get_access(user1) # печатает "User batya99: success"

# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya) # печатает AccessDenied

# Access.get_access(5) # печатает AccessTypeError

class User:
    def __init__(self,name,role) -> None:
        self.name = name
        self.role = role

# class Access:
#     __access_list = ['admin','developer']

#     @staticmethod
#     def __check_access(role): # который принимает название роли и возвращает True если роль находится в списке __access_list , иначе - False
#         if role in Access.__access_list:
#             return True
#         else:
#             return False

#     @staticmethod
#     def get_access(user_): 
#         if not isinstance(user_, User): # который должен принимать экземпляр класса User и проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access
#             print("AccessTypeError")
#         elif Access.__check_access(user_.role): # который должен принимать экземпляр класса User и проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access
#             print(f"User {user_.name}: success")         
#         else:
#             print("AccessDenied")

# Допустим, у нас есть сайт и для успешной регистрации на нем необходимо придумать логин и пароль. Но мы хотим, чтобы при этом выполнялись определенные проверки с предоставленной пользователем информацией, например, чтобы пароль был непростым. Мы можем делегировать данные проверки классу Registration , который вам необходимо создать. 

# Задача будет состоять из двух частей. 

# Часть 1
# Создайте класс Registration, который пока будет проверять только введенный логин. Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

# В классе Registration необходимо реализовать:

# метод __init__ принимающий один аргумент логин пользователя. Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3). То есть когда отработает данный код 
# def __init__(self, логин):
#     self.login = логин # передаем в сеттер login значение логин 
# должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

# Cвойство геттер login, которое возвращает значение self.__login;
 
# Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
# строковое значение, если поступают другие типы данных необходимо вызвать исключение при помощи строки raise TypeError
 
# логин, так как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError
 
# логин должен содержать символ точки «.» после символа «@».В случае, если после @ нету точки, вызываем исключение при помощи строки raise ValueError
# Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login
# Напишите определение класса Registration       
class Registration:
    def __init__(self,login,) -> str:
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self,value):
        if not isinstance(value,str):
            raise TypeError
        elif  not "@" in value:
            raise ValueError
        elif not value.count('@') <=1:
            raise ValueError      
        elif not '.' in value[value.find('@'):]:
            raise ValueError
            
        self.__login = value

# Ниже код для проверки класса Registration


try:
    result = Registration("fga")
except ValueError as error:
    print("Логин fga должен содержать один символ '@'")

try:
    result = Registration(1234)
except TypeError as error:
    print("Пароль должен быть строкой")

try:
    result = Registration("f@ga@")
except ValueError as error:
    print("Логин f@ga@ должен содержать только один символ '@'")

try:
    result = Registration("fg@a")
except ValueError as error:
    print("В логине fg@a должен быть символ '.' после символа '@'")

try:
    result = Registration("fg.@a")
except ValueError as error:
    print("В логине fg.@a должна быть '.' после символа '@'")

result = Registration("translate@gmail.com")
assert result.login == "translate@gmail.com"
assert result._Registration__login == "translate@gmail.com"

try:
    result.login = "asdsa12asd."
except ValueError as error:
    print("Логин asdsa12asd. должен содержать один символ '@'")

try:
    result.login = "asdsa12@asd"
except ValueError as error:
    print("asdsa12@asd должен быть символ '.' после символа '@'")

result.login = "alligator13@how.do"
assert result.login == "alligator13@how.do"
assert result._Registration__login == "alligator13@how.do"
        
            