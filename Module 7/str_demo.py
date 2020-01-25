class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'a {self.color} car having mileage = {self.mileage}'
C1=Car('Red',120)
print(C1)
