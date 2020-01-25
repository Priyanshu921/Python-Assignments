from Vehicle import Automobile
class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.__doors=doors
    def set_doors(self,doors):
        self.self.__doors=doors
    def get_doors(self):
        return self.__doors

t1=Car('volkswagen','Audi',8,8000000,4)
print(t1.get_doors())
