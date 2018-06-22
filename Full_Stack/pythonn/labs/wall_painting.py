# wall_painting.py 06/19/18

import math

print("Hello. We are going to figure out how much it will cost to paint your room.")
print("One gallon of paint covers 400 sq ft.")

def wall_paint():
    width = int(input("How wide is the wall (in feet)?: "))
    height = int(input("How high is the wall (in feet)?: "))
    gallon_cost = float(input("How much does a gallon of paint cost?: $"))
    num_coats = int(input("How many coats of paint will you put on?: "))

    # round number up since you can only buy full gallons of paint
    print("")
    return math.ceil(width * height * num_coats / 400) * gallon_cost

cost = 0
num_walls = int(input("How many walls will you paint? "))
for i in range(num_walls):
    cost += wall_paint()
print("It will cost ${} to paint the room.".format(cost))
