class Adder:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y # а тут складывается (y) аргумент 

a = Adder(10)  # идет в x
b = Adder(20)  # идет в x 
c = a(5) + b(5) # вызыветься метод call в который идет (5) и (5), в у 
print(c)


# Помните из школы это потрясающее уравнение?



# Давайте воссоздадим эту формулу в виде класса QuadraticFunction, в котором есть:

# метод __init__. Он должен сохранять в экземпляр класса три атрибута: a , b и c. 
 
# метод __call__ , который принимает аргумент x, подставляет его в формулу выше, находит значение и возвращает его в качестве результата


class QuadraticFunction:
    def __init__(self,a,b,c) -> int:
        self.a = a
        self.b = b
        self.c = c 

    def __call__(self,x) -> int:
        return self.a * x * x + self.b * x + self.c
        return self.a*x**2 + self.b*x + self.c # x**2 возведение в квадрат 
    

