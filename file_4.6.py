# class Mother:
#     def __init__(self, mother_name):
#         self.mother_name = mother_name


# class Father:
#     def __init__(self, father_name):
#         self.father_name = father_name


# class Child(Mother, Father):
#     def __init__(self, child_name, mother_name, father_name):
#         self.child_name = child_name
#         super().__init__(mother_name)
#         Father.__init__(self,father_name)    
        

#     def introduce(self):
#         return f"Меня зовут {self.child_name}. Моя мама - {self.mother_name}, мой папа - {self.father_name}"


# child = Child("Анна", "Мария", "Иван")
# print(child.introduce())


class Person:
    def __init__(self,name,age) -> str:
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')    

class Company:
    def __init__(self,company_name,location) -> str:
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')

class Employee(Person,Company):
    def __init__(self, name, age,company_name,location) -> str:
        super().__init__(name, age)
        Company.__init__(self,company_name,location)



# Ниже расположены провевки для кода


a = Person('Ivan', 32)
a.display_person_info()

a = Company('Zara', 'Prague')
a.display_company_info()

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()

emp2 = Employee('Kolya', 11, 'Facebook', 'Seatle')
emp2.display_person_info()
emp2.display_company_info()        
