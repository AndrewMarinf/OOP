# Перед вами имеется реализация класса RobotVacuumCleaner. Сейчас над каждым методом стоит знак _.
# Ваша задача сделать код корректным, для это нужно заменить знак _ на один из декораторов @staticmethod, @classmethod и @property или же просто удалить знак

class RobotVacuumCleaner:
    name = 'Henry'
    charge = 25

    # _
    def update_charge(cls, new_value):
        cls.charge = new_value

    # _
    def hello(name):
        return f'Привет, {name}'

    # _
    def data(self):
        return {
            'name': self.name,
            'charge': self.charge
        }

    # _
    def make_clean(self):
        if self.charge < 30:
            return 'Кожаный, заряди меня! Я слаб'
        return 'Я вычищу твою берлогу!!!'

# код ниже не нужно удалять, в нем находятся проверки
print(RobotVacuumCleaner.hello('Господин'))
RobotVacuumCleaner.update_charge(50)

robot = RobotVacuumCleaner()
print(robot.make_clean())
print(robot.data)

RobotVacuumCleaner.update_charge(False)
print(robot.make_clean())