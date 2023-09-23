#  Создайте класс Student, у которого есть:
# конструктор __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;
# приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
# Имя: <name>
# Возраст: <age>
# Направление: <branch>
# метод access_private_method, который вызывает приватный метод __display_details.


class Student:
    def __init__(self,name,age,branch):
        self.__name = name
        self.__age  = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}') # вызывать атрибуты нужнг от экземпляра класса 

    def access_private_method(self):
        self.__display_details()


# Создайте класс BankDeposit, который имеет следующие методы:
# метод __init__, который устанавливает значения атрибутов name, balance и rate: владелец депозита, значение депозита и годовая процентная ставка.
# приватный метод __calculate_profit, который возвращает количество денег, которое получит владелец счета через год с учетом его годовой ставки.
# публичный метод get_balance_with_profit, который возвращает общее количество средств, которое будет у владельца депозита через год.

class BankDeposit:
    def __init__(self,name,balance,rate):
        self.name= name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
            return self.balance * (self.rate/100)

    def get_balance_with_profit(self):
         return self.__calculate_profit() + self.balance # при вызове метода всегда ставить скобки 


        
# Ниже код для проверки методов класса BankDeposit
account = BankDeposit("John Connor", 1000, 5)
assert account.name == "John Connor"
assert account.balance == 1000
assert account.rate == 5
assert account._BankDeposit__calculate_profit() == 50.0
assert account.get_balance_with_profit() == 1050.0

account_2 = BankDeposit("Sarah Connor", 200, 27)
assert account_2.name == "Sarah Connor"
assert account_2.balance == 200
assert account_2.rate == 27
assert account_2._BankDeposit__calculate_profit() == 54.0
assert account_2.get_balance_with_profit() == 254.0
print('Good')