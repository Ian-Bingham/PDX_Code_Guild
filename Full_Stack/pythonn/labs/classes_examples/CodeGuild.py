"""
CodeGuild.py
Define CodeGuild to extend the school class
"""

class School:
	def __init__(self, name, **kwargs):
		self.name = name
		self.instructors = kwargs.pop('instructors', [])
		self.courses = kwargs.pop('courses', [])
		self.students = kwargs.pop('students', [])

	def add_instructor(self, instructor):
		self.instructors.append(instructor)

	def add_course(self, course):
		self.courses.append(course)

	def add_student(self, student):
		self.students.append(student)


# Define this class
class CodeGuild(School):
	def __init__(self, **kwargs):
		super().__init__('CodeGuild', **kwargs)


if __name__ == '__main__':
	kwargs1 = {"instructors": ['Bob', 'Joe', 'Kyle'], "courses": ['math', 'science', 'history'], "students": ['George']}
	arbitrary_school = School('Joy of Painting', **kwargs1)
	arbitrary_school.add_course('Intro to Life and Living')
	arbitrary_school.add_course('Being Kind')
	arbitrary_school.add_course('Bush Rendering')
	arbitrary_school.add_instructor("Bob Ross' Spirit")
	arbitrary_school.add_student('me')
	arbitrary_school.add_student('you')
	print(f"Name: {arbitrary_school.name}")
	print(f"Courses: {arbitrary_school.courses}")
	print(f"Instructors: {arbitrary_school.instructors}")
	print(f"Students: {arbitrary_school.students}")


	# Test your CodeGuild class here
	print("*" * 80)
	kwargs2 = {"instructors": ['a', 'b', 'c'], "courses": ['breakfast', 'lunch', 'dinner']}
	codeguild = CodeGuild(**kwargs2)
	print(f"Name: {codeguild.name}")
	print(f"Courses: {codeguild.courses}")
	print(f"Instructors: {codeguild.instructors}")
	print(f"Students: {codeguild.students}")
