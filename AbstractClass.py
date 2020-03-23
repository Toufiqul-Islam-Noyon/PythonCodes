from abc import ABC, abstractmethod
class Bike(ABC):
    __Bike_Name=None
    __Bike_Price=None
    @abstractmethod
    def display(self): pass
    @abstractmethod
    def calculate_Milage(self): pass

class Honda(Bike):
    def display(self):
        print('Honda is a good bike')

    def calculate_Milage(self):
        print('Honda gives 40 km/l')

#class object
Honda_Obj= Honda()
Honda_Obj.display()
Honda_Obj.calculate_Milage()