# cars.py 6/25/18

class Car(object):
    def __init__(self, color, number_of_doors):
        self.number_of_wheels = 4
        self.color = color
        self.number_of_doors = number_of_doors

    def honk(self):
        print('HONK!')

    def __str__(self):
        return 'Color: {}, Doors: {}, Wheels: {}'.format(self.color, self.number_of_doors, self.number_of_wheels)

    # makes it so line 12 in app.py prints nicely
    def __repr__(self):
        return self.__str__()
