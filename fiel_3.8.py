
# магические методы
# Методы __getitem__ , __setitem__ и __delitem__

# КОД ИЗ УРОКА 
class Vector:

    def __init__(self, *args):
        self.values = list(args) # v1 = Vector(1,2,3,4,5)

    def __repr__(self):
        return str(self.values) # вызов коллекции v1

    def __getitem__(self, item):
        if 0 <= item < len(self.values): #  лежит ли вызов индекса по длине нашей коллекции
            return self.values[item] # если да, вызвать индекс [item], который мы передли сюда. v1[1]
        # if 1 <= item < len(self.values): # это будте индекс от 1 считаться ЛАЙФХАК
        #     return self.values[item-1]
        else:
            raise IndexError('Индекс за границами вашей коллекции')

    def __setitem__(self, key, value):  # изменить индекс. key - это индекс который измен. value - это значение v1[1]=100
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами вашей коллекции')

    def __delitem__(self, key): # удаление del v1[2]
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами вашей коллекции')


# В комментариях присылайте какие вам нравятся здания или можете фотки со своих путешествий. За одно познакомимся)

# Ну а теперь ближе к делу, не зря я про здания заговорил. Нам необходимо создать класс Building. Мы должны научиться создавать здание определенной этажности и уметь бронировать за компанией определенный этаж в здании. Важно, что в нашем классе за одним этажом может быть закреплена только одна компания

# Для этого в классе Building должно быть реализованы

# метод __init__, который принимает количество этажей в здании
# метод __setitem__, который закрепляет за определенным этажом компанию. Если этаж был занят другой компанией, нужно заменить название другой компанией
# метод __getitem__, который возвращает название компании с этого этажа. В случае, если этаж пустует, следует вернуть None
# метод __delitem__, который высвобождает этаж
# В этом задании вы сами решаете какие атрибуты создавать внутри класса, главное реализовать магические методы из списка выше

class Building:

    '''принимает количество этажей в здании'''
    def __init__(self, values):
        self.values = [None]*values

    '''метод __getitem__, который возвращает название компании с этого этажа. 
    В случае, если этаж пустует, следует вернуть None'''

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            return None

    '''закрепляет за определенным этажом компанию. Если этаж был занят другой компанией, 
    нужно заменить название другой компанией'''
    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            return self.values[key]  

    '''высвобождает этаж''' 
    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            self.values[key] = None

iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])





