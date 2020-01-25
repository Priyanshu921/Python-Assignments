from Vehicle import Automobile
class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_types):
        Automobile.__init__(self,make,model,mileage,price)
        self.__drive_types=drive_types
    def set_drive_types(self,drive_types):
        self.self.__drive_types=drive_types
    def get_drive_types(self):
        return self.__drive_types

t1=Truck('Autobots','Optimus',12,200000,'off Road')
print(t1.get_make())
