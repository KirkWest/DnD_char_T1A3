# imports my functions
from functions import create_menu, create_new_character, csv_list, print_char, edit_char

print("Welcome to you Dnd character creator, would you like to")

menu_choice = ""

while menu_choice != "4": #
    menu_choice = create_menu()
    match menu_choice:
        case "1":
            print("You have chosen to create a new character.\n")
            create_new_character() # uses create new character function
            print("Congratulations on creating a new character!!")
            print("")
            print("Is there anything else you'd like to do?") # re prints out the menu list
        case "2":
            csv_files = csv_list()
            print("")
            edit_char(csv_files)
            print("")
            print("Is there anything else you'd like to do?")

        case "3":
            print("Below is a list of characters you have available to view")
            csv_files = csv_list()
            print("")
            print_char(csv_files)
            print("")
            print("Is there anything else you'd like to do?")
            
        case "4":
            print("Thankyou for using DnD character creator")
        case _:
            print("Please enter a number from 1-4.")
    
# Add in some colour and tidy up the formatting, if time try and incorporate DRY in spots that might be reusing same code

# dropped re-roll, leaving it to just edit if the user doesn't like their stats or needs to update on level up.