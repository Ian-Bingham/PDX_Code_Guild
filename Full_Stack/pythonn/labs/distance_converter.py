# distance_converter.py 06/19/18

distance = int(input("Enter a numerical distance to convert.\n> "))
units = input("Enter the units of that distance (mi, km, ft, m).\n> ")
target_units = input("Enter the units you would like to convert to (mi, km, ft, m).\n> ")

def convert_distance(distance, units, target_units):
    if units == target_units:
        print("No conversion needed.")
        exit(0)
    if units == "mi":
        if target_units == "km":
            converted_distance = distance / 0.62137
        if target_units == "ft":
            converted_distance = distance * 5280
        if target_units == "m":
            converted_distance = distance / 0.00062137
    if units == "km":
        if target_units == "mi":
            converted_distance = distance * 0.62137
        if target_units == "ft":
            converted_distance = distance * 3280.8
        if target_units == "m":
            converted_distance = distance * 1000
    if units == "ft":
        if target_units == "km":
            converted_distance = distance / 3280.8
        if target_units == "mi":
            converted_distance = distance / 5280
        if target_units == "m":
            converted_distance = distance / 3.2808
    if units == "m":
        if target_units == "km":
            converted_distance = distance / 1000
        if target_units == "ft":
            converted_distance = distance * 3.2808
        if target_units == "mi":
            converted_distance = distance * 0.00062137

    print(f"{distance} {units} is {converted_distance} {target_units}")

convert_distance(distance, units, target_units)
