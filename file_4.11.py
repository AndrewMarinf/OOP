from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self,hours_worked, hourly_rate) -> None:
        super().__init__()
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class SalariedEmployee(Employee):
    def __init__(self,monthly_salary) -> None:
        super().__init__()
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
    
        


