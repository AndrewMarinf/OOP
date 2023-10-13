
# try:
#     a = int(input())
#     b = int(input())
#     print(f"Результат деления a на b: {a/b}")
# except (ValueError,ZeroDivisionError):
#     print('Введите корректные значения')  


class CustomButton:
    def __init__(self,text,*kwargs) -> None:
        self.text = text
        self.kwargs = list(*kwargs) 
    
    
    def config(self,*kwargs):
        self.kwargs = kwargs

    try:
        def click(self):
            self.command()
    except (AttributeError):
        print('Кнопка не настроена')

    except  TypeError:
        print('Кнопка сломалась')



