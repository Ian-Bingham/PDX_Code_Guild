# cars.py 6/25/18


class Car(object):
    def __init__(self, color, num_doors):
        self.num_wheels = 4
        self.color = color
        self.num_doors = num_doors

    @staticmethod
    def honk():
        print('HONK!')

    def __str__(self):
        return 'Color: {}, Doors: {}, Wheels: {}'\
                 .format(self.color, self.num_doors, self.num_wheels)

    # overrides how print works for Car objects
    def __repr__(self):
        return self.__str__()
