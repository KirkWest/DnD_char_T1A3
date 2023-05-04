# imports my functions
from functions import create_menu, create_new_character, csv_list, print_char

print("Welcome to you Dnd character creator, would you like to")

menu_choice = ""

while menu_choice != "4": #
    menu_choice = create_menu()
    match menu_choice:
        case "1":
            print("You have chosen to create a new character.\n")
            create_new_character() # uses create new character function
            print("What would you like to do now?") # re prints out the menu list
        case "2":
            csv_list()
            print("")
            print("Which character would you like to edit?")

        case "3":
            print("Below is a list of characters you have available to view")
            csv_files = csv_list()
            print("")
            print_char(csv_files)
            print("")
            
        case "4":
            print("Thankyou for using DnD character creator")
        case _:
            print("Please enter a number from 1-4.")
    
# printing the csv files available to access is done, next I need to be able to access a chosen character
# print out said character in the terminal then edit class or stats.

# need to add in a re-roll option for attributes(might leave this as part of the edit section)
# print all characters created as per option 3