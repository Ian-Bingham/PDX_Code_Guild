# hammer.py 6/18/18


# assumes user types in correct input EVERY time: 10AM, 6PM
def hammer_time():
    time = input("What time is it?\n> ").replace(" ", "").lower()
    hour = int(time[:-2])  # get the hour
    meridiem = time[-2:]  # get am or pm

    # Breakfast: 7AM - 9AM
    # Lunch: 12PM - 2PM
    # Dinner: 7PM - 9PM
    # Hammer: 10PM - 4AM
    if 7 <= hour <= 9 and meridiem == "am":
        print("It's breakfast time!")
    elif hour in [12, 1, 2] and meridiem == "pm":
        print("It's lunch time!")
    elif 7 <= hour <= 9 and meridiem == "pm":
        print("It's dinner time!")
    elif (hour in [10, 11] and meridiem == "pm") or \
         (hour in [12, 1, 2, 3, 4] and meridiem == "am"):
        print("It's hammer time!")
    else:
        print("Take a break from eating!")

hammer_time()
