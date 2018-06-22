# grading.py 6/6/18

def grading():
    grade = int(input("Type in a number between 0 and 100. > "))

    letter_grade = ''
    if grade in range(90, 101):
        letter_grade = 'A'
    elif grade in range(80, 91):
        letter_grade = 'B'
    elif grade in range(70, 81):
        letter_grade = 'C'
    elif grade in range(60, 71):
        letter_grade = 'D'
    elif grade in range(0, 61):
        letter_grade = 'F'
    else:
        print("The number entered was not between 0 and 100. Exiting program.")
        exit(0)

    if grade in range(50, 101):
        if grade % 10 <= 3:
            letter_grade += '-'
        elif grade % 10 >= 7:
            letter_grade += '+'
    elif grade in range(0, 50):
        letter_grade += '-'

    print("Your grade is " + letter_grade)

grading()
