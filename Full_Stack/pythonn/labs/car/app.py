# app.py 6/25/18

from car import Car

# only runs if this is the file being executed
if __name__ == '__main__':
    car1 = Car('Red', 2)
    car2 = Car('Blue', 1)
    car3 = Car('Yellow', 5)

    print(car1)
    print(car2)
    print(car3)
