# imports my functions
from functions import create_menu, print_csv, create_new_character

print("Welcome to you Dnd character creator, would you like to")

menu_choice = ""

while menu_choice != "4": #
    menu_choice = create_menu()
    match menu_choice:
        case "1":
            print("You have chosen to create a new character.\n")
            create_new_character()
            print("What would you like to do now?") # re prints out the menu list
        case "2":
            print_csv()
            print("")
            print("Which character would you like to edit?")

        case "3":
            print("You have chosen to see a list of created characters.")
        case "4":
            print("Thankyou for using DnD character creator")
        case _:
            print("Please enter a number from 1-4.")
    
# printing the csv files available to access is done, next I need to be able to access a chosen character
# print out said character in the terminal then edit class or stats.

# need to add in a re-roll option for attributes(might leave this as part of the edit section)
# print all characters created as per option 3