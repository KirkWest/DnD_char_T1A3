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
    


 
 # need to add in a re-roll option for attributes(might leave this as part of the edit section)
 # need to create the file handling part
 # once file handling is built create an edit character functions as per option 2 and
 # print all characters created as per option 3