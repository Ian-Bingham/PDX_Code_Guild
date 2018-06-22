# functions.py 06/19/18

def hi():
    print("Hi!")

def greeting(foo):
    print(f"Hello, {foo}. How are you today?")

hi()
name = input("What is your name?\n> ")
greeting(name)

print(chr(100))
print(ord('d'))

fruit = ["apples", "banana", "grapes"]
print(list(enumerate(fruit)))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = filter(lambda x: x % 2 == 0, nums) # lambda creates an anonymous function (only one line of code)
print(list(filtered))
