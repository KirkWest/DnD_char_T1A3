# imports my functions
from functions import create_menu, dice_roll, char_name, print_class


attribute_scores = {}
attribute_names = ["strength", "dexterity", "constitution", "intelligence", "wisdom" "charisma"]
print("Welcome to you Dnd character creator, would you like to")

print(create_menu())

print(char_name())

choice = print_class()
print("you've chosen the " + choice + " class")

attribute_names = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

for a in attribute_names:
    score = dice_roll(4)
    attribute_scores[a] = score
print(f"Welcome, {char_name} the {print_class}, below are your attributes:")

 # need to finish the dice roll attribute allocation

 # need to add in a re-roll option for attributes
 # need to create the file handling part
 # once file handling is built create an edit character functions as per option 2 and
 # print all characters created as per option 3