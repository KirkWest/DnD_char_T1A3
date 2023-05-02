# imports my functions
from functions import create_menu, dice_roll, char_name, print_class


attribute_scores = {}
attribute_names = ["strength", "dexterity", "constitution", "intelligence", "wisdom" "charisma"]
print("Welcome to you Dnd character creator, would you like to")

menu_choice = ""

while menu_choice != "4":
    menu_choice = create_menu()

    match menu_choice:
        case "1":
            print("You have chosen to create a new character.\n")
            name = char_name()
            char_class = print_class()
            attribute_names = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            attribute_scores = {}
            for a in attribute_names:
                score = dice_roll(4)
                attribute_scores[a] = score
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            # clears the terminal for a cleaner display of the final results
            print("Thank you for using Dnd Character Creator")
            print(f"Character name: {name}")
            print(f"Character class: {char_class}\n")
            print("Below are your attribute scores:")
            for key, value in attribute_scores.items():
                print(key+str(":"), value)
                print("")
                print("What would you like to do now?")
        case "2":
            print("You have chosen to edit a previous character.")
        case "3":
            print("You have chosen to see a list of created characters.")
        case "4":
            print("Thankyou for using DnD character creator")
        case _:
            print("Please enter a number from 1-4.")
    


 # need to finish the dice roll attribute allocation

 # need to add in a re-roll option for attributes
 # need to create the file handling part
 # once file handling is built create an edit character functions as per option 2 and
 # print all characters created as per option 3