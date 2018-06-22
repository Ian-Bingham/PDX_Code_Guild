# madlib.py 6/18/18

import random

def madlib():
    print("Hello. This is a madlib program.")
    names = input("Please enter two names separated by commas.\n> ")
    places = input("Please enter two places separated by commas.\n> ")
    adjectives = input("Please enter three adjectives separated by commas.\n> ")
    verbs = input("Please enter two verbs separated by commas.\n> ")
    foods = input("Please enter two foods separated by commas.\n> ")

    names_list = list(names.replace(" ", "").split(","))
    places_list = list(places.replace(" ", "").split(","))
    adjectives_list = list(adjectives.replace(" ", "").split(","))
    verbs_list = list(verbs.replace(" ", "").split(","))
    foods_list = list(foods.replace(" ", "").split(","))

    random.shuffle(names_list)
    random.shuffle(places_list)
    random.shuffle(adjectives_list)
    random.shuffle(verbs_list)
    random.shuffle(foods_list)

    story_time = input("Would you like to hear the story I created (again)?\n> ")

    while True:
        if story_time.lower() == "yes" or story_time.lower() == "y":
            print(
f"""One day my friend {names_list[0]} and I went to the {places_list[0]}.
He was wearing a {adjectives_list[0]} coat and {adjectives_list[1]} shoes
while I wore nothing but {adjectives_list[2]} underwear.
Once there we met up with our other friend {names_list[1]} and ate some {foods_list[0]}.
It was delicious! To burn off the calories we planned to go to {places_list[1]} and do some {verbs_list[0]},
but instead we sat around and ate some {foods_list[1]}...
We'll make up for it by going {verbs_list[1]} tomorrow."""
            )
        elif story_time.lower() == "no" or story_time.lower() == "n":
            break

        story_time = input("\nWould you like to hear the story I created (again)?\n> ")

    new_story = input("Would you like to make a new story?\n> ")
    if new_story == "yes" or new_story == "y":
        madlib()
    elif new_story == "no" or new_story == "n":
        print("Alright. Thanks for playing!")
        exit(0)

madlib()
