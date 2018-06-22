# list_examples.py 6/18/18

fruit = ["apple", "banana", "orange", ["grapes", "kiwi"]]
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[len(fruit) - 1]) # last item in list
print(fruit[-1]) # last item in list
print(fruit[-2]) # second to last item in list
print(fruit[1:2:1]) # [start:stop:step] includes start, does not include stop
print(fruit[3][1]) # prints kiwi
print(fruit[-1][-1]) # prints kiwi

fruit.append(["watermelon", "starfruit", "guava"])
print(fruit)

removed_thing = fruit.pop(0)
print(removed_thing)
print(fruit[0])


# tuples - constant list
tup = ("thing", 123, ["first", "middle", "last"])
print(tup[0])
print(tup[-1])
print(tup[1:])
# tup[1] = 456 - ERROR. cant modify constant list
# tup.append("blah") - ERROR. cant modify constant list
tup[-1][1] = "newMiddle" # totally valid!!! lists in tuples CAN be modified
