# Создайте класс BankAccount, который имеет следующие методы:
# метод __init__, который устанавливает значения атрибутов _account_number  и _balance: номер счета и баланс
# геттер-метод для атрибута _account_number
# геттер-метод для атрибута _balance
# сеттер-метод для атрибута _balance


# Напишите определение класса BankAccount       
class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self,):
        return self._account_number
        

    def get_balance(self):
        return self._balance
    
    def set_balance(self,value):
        self._balance = value

# Ниже код для проверки методов класса BankAccount
account = BankAccount("1234567890", 1000)
assert account._balance == 1000
assert account._account_number == "1234567890"
assert account.get_account_number() == "1234567890"
assert account.get_balance() == 1000
account.set_balance(1500)
assert account.get_balance() == 1500

print('Good')


# Создайте класс Employee, который имеет следующие методы:
# метод __init__, который устанавливает значения приватных атрибутов __name  и __salary: имя работника и его зарплату
# приватный геттер метод для атрибута __name
# приватный геттер метод для атрибута __salary
# приватный сеттер метод для атрибута __salary: он должен позволять сохранять в атрибут __salary только положительные числа. В остальных случаях не сохраняем переданное значение в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
# свойство title, у которого есть только геттер из пункта 2.
# свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.


      
class Employee:
    def __init__(self,name,salary) -> None:
        self.__name = name
        self.__salary = salary

    def get__name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    # def set__salary(self,value): # эта функция не идет 
    #     if not  isinstance(value,( int,float) and value >= 0):
    #         print(f'ErrorValue:{value}')
    #     else:
    #         self.__salary = value

    def __set_salary(self,value):
        if  isinstance(value,( int,float))and value >= 0:
            self.__salary = value
        else:   
            print(f'ErrorValue:{value}')    


    title = property(fget=get__name)
    reward = property(fget=__get_salary,fset=__set_salary)  

# Ниже код для проверки методов класса Employee
employee = Employee("John Doe", 50000)
assert employee.title == "John Doe"
assert employee._Employee__name == "John Doe"
assert isinstance(employee, Employee)
assert isinstance(type(employee).title, property), 'Вы не создали property title'
assert isinstance(type(employee).reward, property), 'Вы не создали property reward'

assert employee.reward == 50000
employee.reward = -100  # ErrorValue:-100

employee.reward = 1.5
assert employee.reward == 1.5

employee.reward = 70000
assert employee.reward == 70000
employee.reward = 'hello'  # Печатает ErrorValue:hello
employee.reward = '777'  # Печатает ErrorValue:777
employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
assert employee.reward == 70000
employee._Employee__set_salary(55000)
assert employee._Employee__get_salary() == 55000