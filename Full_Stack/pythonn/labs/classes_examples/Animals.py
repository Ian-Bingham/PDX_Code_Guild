"""
Animal.py

Extend the Animal class with two animal subclasses.
"""


class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def move(self):
        print(f'{self.name} moves.')

    def __repr__(self):
        return f'{self.name} is a {self.species}.'


# Bird inherits from Animal
class Bird(Animal):
    # get all of the same methods in Animal
    def __init__(self, name):
        super().__init__('bird', name)

    # override move method from Animal class
    def move(self):
        print(f'{self.name} flaps.')


class Cat(Animal):
    # get all of the same methods in Animal
    def __init__(self, name):
        super().__init__('cat', name)

    # override move method
    def move(self):
        print(f'{self.name} walks.')

    # create a new method called talk()
    def talk(self):
        print(f'{self.name} says meow!')


class Eagle(Bird):
    # get all of the same methods in Bird
    def __init__(self, name):
        super().__init__(name)

    # create a new method called merica()
    def merica(self):
        print(f"{self.name} flies around carrying a US flag and bacon.")


class Tiger(Cat):
    # get all of the same methods in Cat
    def __init__(self, name):
        super().__init__(name)

    # inherit the move method, but add more to it
    def move(self):
        super().move()
        print(f"{self.name} also stalks its prey")


if __name__ == '__main__':
    print("*" * 20)
    arbitrary_animal = Animal('jackalope', 'lucy')
    print(arbitrary_animal)
    arbitrary_animal.move()

    print("*" * 20)
    bird = Bird('screaming boy')
    print(bird)
    bird.move()

    # Test your animal here
    print("*" * 20)
    cat = Cat("Sammy")
    print(cat)
    cat.move()
    cat.talk()

    print("*" * 20)
    eagle = Eagle("Caw Caw")
    print(eagle)
    eagle.move()
    eagle.merica()

    print("*" * 20)
    tiger = Tiger("Tony")
    print(tiger)
    tiger.move()
    tiger.talk()
