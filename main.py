# Main file that should control my application

# imports my functions

from functions import create_menu, create_new_character, csv_list, print_char, edit_char
from colored import fg, bg, attr


print(f"{fg('blue')}Welcome to your Dnd character creator, would you like to{attr('reset')}")

menu_choice = ""

while menu_choice != "4": #
    menu_choice = create_menu()
    match menu_choice:
        # case 1 is for creating a character
        case "1": 
            print(f"You have chosen to {fg('green')}create{attr('reset')} a new character.\n ")
            create_new_character() # uses create new character function
            print("Congratulations on creating a new character!!")
            print("")
            print(f"{fg('blue')}Is there anything else you'd like to do?{attr('reset')}") # re prints out the menu list

        # case 2 is for edit character function
        case "2": 
            print(f"You have chosen to {fg('green')}edit{attr('reset')} a character.\n")
            csv_files = csv_list()
            if not csv_files:
                print("")
                print(f"{fg('blue')}Returning to main menu...{attr('reset')}")
                continue
            print("")
            edit_char(csv_files)
            print("")
            print(f"{fg('blue')}Is there anything else you'd like to do?{attr('reset')}")
        
        # case 3 is for the view character function
        case "3": 
            print(f"Below is a list of characters you have available to {fg('green')}view{attr('reset')}")
            csv_files = csv_list()
            if not csv_files:
                print("")
                print(f"{fg('blue')}Returning to main menu...{attr('reset')}")
                continue
            print("")
            print_char(csv_files)
            print("")
            print(f"{fg('blue')}Is there anything else you'd like to do?{attr('reset')}")
        
        # case 4 is to exit the program    
        case "4": 
            print(f"{fg('blue')}Thankyou for using DnD character creator{attr('reset')}")

        # if user enters an invalid choice it will loop back to this to ask again
        case _: 
            print(f"{fg('red')}Please enter a number from 1-4{attr('reset')}")
    
# Add in some colour and tidy up the formatting, if time try and incorporate DRY in spots that might be reusing same code

# dropped re-roll, leaving it to just edit if the user doesn't like their stats or needs to update on level up.