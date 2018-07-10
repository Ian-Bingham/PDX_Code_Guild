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


class Bird(Animal):
	def __init__(self, name):
		super().__init__('bird', name)

	def move(self):
		print(f'{self.name} flaps.')


class Cat(Animal):
	def __init__(self, name):
		super().__init__('cat', name)

	def move(self):
		print(f'{self.name} walks.')

	def talk(self):
		print(f'{self.name} says meow!')


class Eagle(Bird):
	def __init__(self, name):
		super().__init__(name)

	def move(self):
		super().move()

	def merica(self):
		print(f"{self.name} flys around carrying a US flag and bacon.")

class Tiger(Cat):
	def __init__(self, name):
		super().__init__(name)

	def move(self):
		super().move()
		print(f"{self.name} also stalks its prey")

	def talk(self):
		super().talk()



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
