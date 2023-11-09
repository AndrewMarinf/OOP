
class Zebra():
    count = 0
    def which_stripe(self):
        if self.count % 2 == 0:
            print("Полоска белая")
            
        else: 
            print("Полоска черная")
        self.count += 1       
    print(count)
    
z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая 

# =====================================================================
class Person:
    def __init__(self,first_name,last_name,age) -> str:
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def is_adult(self):
        if self.age >= 18:
            return True
        return False


# Ниже код для проверки методов класса Person
p1 = Person('Ash', 'Ketchum', 20)
assert isinstance(p1, Person)
assert p1.full_name() == 'Ketchum Ash'
assert p1.age == 20
assert p1.first_name == 'Ash'
assert p1.last_name == 'Ketchum'
assert p1.is_adult() is True

p2 = Person('Hermione', 'Granger', 16)
assert isinstance(p2, Person)
assert p2.age == 16
assert p2.first_name == 'Hermione'
assert p2.last_name == 'Granger'
assert p2.full_name() == 'Granger Hermione'
assert p2.is_adult() is False   
print('Good')

# ====================================================================


class Stack:
    def __init__(self) -> None:
        self.values = []

    def push(self,item):
        self.values.append(item)
    
    # 1 варик тупил 
    def pop(self):
        if len(self.values) == 0:
            print('Empty Stack')  
        else: 
            removed = self.values.pop()
            return removed 

    # 2 варик        
    def pop(self):
        if self.value:
            return self.value.pop()
        print("Empty Stack")             


    def peek(self):
        if not len(self.values)== 0:
            return self.values[-1]
        else: print('Empty Stack')
        return None       
        
    def is_empty(self):
        if not self.values:
            return True
        return False
    
    def size(self):
        return len(self.values)
    

# Вариант №2. Избежал дублирование кода в методах peek и pop
class Stack:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return not self.size()

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.peek():
            return self.values.pop(-1)

    def peek(self):
        if not self.is_empty():
            return self.values[-1]
        print('Empty Stack')




s = Stack()
assert s.values == []
assert isinstance(s, Stack)

s.peek()  # распечатает 'Empty Stack'
assert s.is_empty() is True
s.push('cat')
assert s.size() == 1
assert s.peek() == 'cat'

s.push('dog')
assert s.size() == 2
assert s.peek() == 'dog'

s.push(True)
assert s.size() == 3
assert s.is_empty() is False

s.push(777)
assert s.size() == 4

assert s.pop() == 777
assert s.size() == 3

assert s.pop() is True
assert s.size() == 2

s.push(123)
s.push(123456)
assert s.peek() == 123456
assert s.size() == 4

assert s.pop() == 123456
assert s.pop() == 123
assert s.pop() == 'dog'
assert s.is_empty() is False
assert s.pop() == 'cat'
assert s.is_empty() is True


d = Stack()
assert d.peek() is None  # Печатает "Empty Stack"
assert d.pop() is None  # Печатает "Empty Stack"
d.push('hello')
assert d.size() == 1
d.push('world')
assert d.size() == 2
assert d.peek() == 'world'
assert d.pop() == 'world'
assert d.peek() == 'hello'




# ====================================================================================================

persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]

class Worker:
    
    def __init__(self,name,salary,gender,passport) -> str:
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print (f'Worker {self.name}; passport-{self.passport}')


worker_objects = []
for i in persons:
    worker_objects.append(Worker(*i))
    # worker_objects.append(Worker(name,salary,gender,passport)) # туда идут эти атрибуты вместо *
    print(worker_objects)
    Worker(*i).get_info()


    
class CustomLabel:
    
    def __init__(self,master,**kw) -> None:
        self.text = master
        for key,value in kw.items():
            self.__dict__[key] = value


    def config(self,**kw):
        self.__dict__.update(kw)
# ===========================================================================================================================================       

class Person:

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:

    def __init__(self,company_name,location) -> None:
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')  

class Employee:

    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)


# ===================================================================================================
#  не решил 2.3 задача
class Task:
    def __init__(self,name,description,status) -> str:
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print(f'​​​​​{self.name} {self.status}')


class TaskList:
    
    def __init__(self) -> str:
        self.tasks = []

    def add_task(self,a):
        self.tasks.append(a)

    def remove_task(self,b):
        self.tasks.remove(b)

class TaskManager:
    def __init__(self,) -> str:
        pass

# ==============================================================================================
# 
#                 










