# Пример в интернете

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0: #  проверяющее, не пуст ли стек
            return None
        removed = self.stack.pop() #  Мы будем сохранять этот элемент(который удаляют) в переменную removed
        return removed # , а затем возвращать переменную

    def push(self,item):
        self.stack.append(item)


class Stack:
    "Класс для стека"

    def __init__(self):
        self.values = []
       
    "метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает"
    def push(self, item):
        self.values.append(item)

    "метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод ***возвращает элемент***. Стек изменяется. Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "
    def pop(self):
        if self.peek():
            return self.values.pop(-1)
    "возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется. Если элементов в стеке нет, распечатайте сообщение "
    def peek(self):
        if not self.is_empty():
            return self.values[-1]
        print('Empty Stack')
      
    "метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение."
    def is_empty(self):
        return not self.size()

    "метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число."
    def size(self):
        return len(self.values)      
    
    def pas(self):
        pass