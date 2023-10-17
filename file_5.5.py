


class BamkAccount():
    def __init__(self,balance) -> int:
        self.balance = balance


class NegativeDepositError(Exception):
    pass

def deposit(self,value):
    if self.value < 0:
        raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
    else: 
        self.balance += self.value
              
             

class InsufficientFundsError(Exception):
    pass    
    
    
    def withdraw (self):
        pass








