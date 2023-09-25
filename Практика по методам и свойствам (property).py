
from string import digits # в digits хронятья все цифры в в виде стркои '0123456789'

class User:
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password # назвали как SET функцию, чтобы сразу пошли проверки на пароль что он содержит, то что нужно

#есть доступ в не класса к атрибуту password. 
# Это не правильно, можно будет его изменять 

    @property #это GET (метод получить значение) функция отлавливает  если хотят получить атрибут.. который не дожен показываться 
    def password(self): # название одинаковое с перменной и SETOROM
        return self.__password
    

    @staticmethod # он нужен чтобы self не принимался потому что по умолчанию будет self, ее можно написать и в не класса, а нужен только password.
    # Это функция просто будет в области видимости класса
    def is_include_number(password):
        for i in digits:
            if i in password: # есть ли цифра в пароле или нет 
                return True
        return False
    
    @staticmethod
    def ppassword_verification(password): # проверяем вводит ли user популярный пароль
        with open('pass.txt','r') as pas: # откройте файл в режиме чтения
            # word = pas.read().split() # можно без split # прочитать содержимое файла и разбиваем
            if password in pas.read():  # пишем read(), а то читать не будет !!!!!! ,word тогда надо сюда писать # проверьте, присутствует ли слово или нет
                return True
            return False
        
    @password.setter # это SET (установка значение) это нужно чтобы защитить и удобно вызывать 
    def password(self,value):
        if not isinstance(value,str): # если тип нашего значения не пренадлежит str
            raise TabError('Пароль должен быть стракой') # то вызываем исключение
        elif len(value) < 4:
            raise ValueError('Длина пароля слишком мала')
        elif len(value) > 12:
            raise ValueError('Длина пароля слишком велика')
        elif not User.is_include_number(value): # если функция не сработала и верне False 
            raise TabError('Пароль должен содержать хотябы одну цифру')
        elif User.ppassword_verification(value):      #!!!!!!!!!!!!!!!!!!!!!!!!!!!! тут новый код 
            raise TabError('Популярный пароль ')
        
        self.__password = value # эта строчка не запишиться никогда



A = User('Ivan','123123')