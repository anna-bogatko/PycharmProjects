"""
Object Oriented Programming
"""

class Car(object):

    wheels = 4

    #Method __init__ allows to use all attributes, methods for object
    def __init__(self, make, model):
        self.make_car = make
        self.model_of_car = model

    def info(self):
        print("Make of the car: " + self.make_car)
        print("Model of the car: " + self.model_of_car)

print(Car.wheels)
c1 = Car('bmw', '550i')
c1.info()

c2 = Car('subaru', 'E350')
c2.info()
