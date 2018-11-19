
class Fruit(object):
    def __init__(self):
        print("The fruit class was created")

    def nutrition(self):
        print("Fruits are good for breakfast")

    def fruit_shape(self):
        print("Fruits can be of any shape except square")


class Pineapple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("This is a class for pineapple")

    def nutrition(self):
        print("Pineapple has a very good impact on nutrition")

    def color(self):
        print("Pineapple is yellow inside")


f = Fruit()
f.nutrition()
f.fruit_shape()

print("#" * 90)

p = Pineapple()
p.nutrition()
p.fruit_shape()
p.color()
