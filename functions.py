import os # imports library for splitting the file to remove .csv
import csv
import random # imports library for my dice roll function
import glob # imports library to search for any csv files (characters already created)

# attribute_scores = {}
# attribute_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom" "Charisma"]

def create_menu():
    print("1. Create new character enter 1")
    print("2. Edit previous character enter 2")
    print("3. See list of created characters enter 3")
    print("4. Exit enter 4")
    print("")
    menu_choice = input("Type the number (1-4): ")
    print("")
    return menu_choice
    
# character name input def
def char_name():
    name = input("What name would you like to call your character?: ")
    print("")
    return name
    
# made the classes a dictionary to clean it up, this way I can let the user just input an integer value
# to select the class but only returns the class name. Hopefully cleaner for file handling
def print_class():
    classes = {"1": "Barbarian",
               "2": "Bard",
               "3": "Cleric",
               "4": "Druid",
               "5": "Fighter",
               "6": "Monk",
               "7": "Paladin",
               "8": "Ranger",
               "9": "Rogue",
               "10": "Sorcerer",
               "11": "Warlock",
               "12": "Wizard"
               }
    print("Class list")
    for i, c in classes.items():
        print(f"{i}. {c}")
    choice = input("Which class would you like? Choose from the above (1-12): ")
    return classes.get(choice)

# dice roll function, rolls a certain amount of dice to be specified then removes the
# lowest number as per DnD rules (usually 4 die, so only count the top 3 scores count)
def dice_roll(num_dice):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, 6))
    rolls.remove(min(rolls))
    return sum(rolls)

# creates the character from all the inputs and writes to csv file
def create_new_character():
    name = char_name()
    char_class = print_class()
    attribute_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    attribute_scores = {}
    for a in attribute_names:
        score = dice_roll(4)
        attribute_scores[a] = score
    os.system('cls' if os.name == 'nt' else 'clear')
    # clears the terminal for a cleaner display of the final results
    print("Thank you for using Dnd Character Creator")
    print(f"Character name: {name}") # prints character name input
    print(f"Character class: {char_class}\n") # character class chosen
    print("Below are your attribute scores:")
    for key, value in attribute_scores.items():
        print(key+str(":"), value) # turns the attributes and the rolled stats to a dictionary
    with open(f"{name}.csv", mode = "w", newline = "") as file: # creates the csv file under the characters name
        writer = csv.writer(file)
        writer.writerow(["Name", name]) # writes in characters name
        writer.writerow(["Class", char_class]) # writes in characters class
        for key, value in attribute_scores.items():
            writer.writerow([key, value]) # writes in characters attributes
        print("")

# using glob import to find and print out any characters already made into the terminal
def csv_list():
    csv_files = glob.glob("*.csv")
    print("Current list of characters: \n")
    for file in csv_files:
        name_only = os.path.splitext(file)[0] # removes the .csv from the print
        print(name_only)
    return csv_files


def edit_char(csv_files):
    csv_files_lower = [file.lower() for file in csv_files] # changes csv file names to lower case when it compares them to the user input
    while True:
        char_choice = input("Which character would you like to edit? Please enter their name: ").lower() # turns user input to lowercase to match the previous function so the search isn't case sensitive
        print("")
        char_file = f"{char_choice}.csv".lower() # uses the user input when searching selecting the file
        if char_file.lower() in csv_files_lower:
            with open(char_file, mode = "r") as file: # opens file in read mode
                reader = csv.reader(file)
                char_info = []
                for row in reader:
                    row[0] = row[0].lower() # turns to lowercase for user error in input
                    print(row)
                    char_info.append(row)
                changes = True # creates additional changes loop
                while changes:
                    while True:
                        try: # try block for error handling
                            value_to_edit = input("What would you like to edit? e.g Class or Strength etc: ").lower() # user input for slecting what key they want to change the value of
                            if value_to_edit.lower() not in [row[0] for row in char_info]:
                                raise ValueError("That doesn't exist, try again") # raises error if input doesn't anything in the file
                            break
                        except ValueError as error:
                            print(error)
                    while True:
                        new_value = input("Please enter the change: ") # if user input matches a key then asks what to change value to
                        for i in range(len(char_info)):
                            if value_to_edit.lower() == char_info[i][0]:
                                char_info[i][1] = new_value.capitalize() # capilizes the class name the user puts in to match the original class list
                        with open(char_file, mode = "w", newline = "") as file:
                            writer = csv.writer(file)
                            writer.writerows(char_info)
                        changes_prompt = input("Any additional changes? y/n: ").lower() #lets the user make additional changes
                        if changes_prompt  == "n":
                            changes = False
                            print("Great changes!")
                            break # breaks inner loop
                        elif changes_prompt == "y":
                            break # loops back through the slecect key to change value of again
            return
        print("That character does not exist, try again")


# function to print out a csv file the user has selected in view or edit meu options
def print_char(csv_files):
    csv_files_lower = [file.lower() for file in csv_files]
    while True: # loops back if name input is wrong
        char_choice = input("Please enter the name of the character you would like view: ").lower()
        char_file = f"{char_choice}.csv".lower()
        if char_file.lower() in csv_files_lower:
            with open(char_file, mode = "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
            break
        else:
            print(f"That character does not appear to exist, try again \n")

