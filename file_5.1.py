
class Wallet():
    def __init__(self, currency, balance) -> None:
        self.currency = currency
        self.balance = balance

    @currency.setter
    def currency(self,value):
        if not isinstance(value,str):
            raise TabError ("Неверный тип валюты")
        elif len(value) == 3:
            raise NameError ( "Неверная длина названия валюты")
        elif not value.isupper():
            raise ValueError ("Название должно состоять только из заглавных букв")
        
        self.currency = value

    def __eq__(self):
        if pass :
            raise ValueError ("Нельзя сравнить разные валюты")
        elif Wallet == self:
            raise TypeError (f"Wallet не поддерживает сравнение с {self}")
        
    def __add__(self):
        pass
            



         
        
