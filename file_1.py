# Создайте класс Contact, у которого есть:
#атрибут name, со значением 'Barak'
#атрибут phone_number, со значением '+1 202 345 4564'
#Создайте ЭК и сохраните его в переменную b
class Contact:
    name = 'Barak'
    phone_number = '+1 202 345 4564'
b = Contact()

# У нас имеется пустой класс Animal и его экземпляр, хранящийся в переменной lion.
# Допишите код,  чтобы функция isinstance смогла проверить, принадлежит ли lion классу Animal
class Animal:
    pass

lion = Animal()
print(isinstance(lion,Animal))