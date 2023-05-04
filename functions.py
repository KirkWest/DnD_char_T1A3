import os # imports library for splitting the file to remove .csv
import csv

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
    import random # imports library for my dice roll function
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
    import glob # imports library to search for any csv files (characters already built)
    csv_files = glob.glob("*.csv")
    print("Current list of characters: \n")
    for file in csv_files:
        name_only = os.path.splitext(file)[0] # removes the .csv from the print
        print(name_only)
    return csv_files


def edit_char(csv_files):
    csv_files_lower = [file.lower() for file in csv_files]
    while True:
        char_choice = input("Which character would you like to edit? Please enter their name: ").lower()
        print("")
        char_file = f"{char_choice}.csv".lower()
        if char_file.lower() in csv_files_lower:
            with open(char_file, mode = "r") as file:
                reader = csv.reader(file)
                char_info = []
                for row in reader:
                    row[0] = row[0].lower()
                    print(row)
                    char_info.append(row)
                changes = True # creates additional changes loop
                while changes:
                    while True:
                        try: # try block for error handling
                            value_to_edit = input("What would you like to edit? e.g Class or Strength etc: ").lower()
                            if value_to_edit.lower() not in [row[0] for row in char_info]:
                                raise ValueError("That doesn't exist, try again") # raises error if input doesn't anything in the file
                            break
                        except ValueError as error:
                            print(error)
                    while True:
                        new_value = input("Please enter the change: ")
                        for i in range(len(char_info)):
                            if value_to_edit.lower() == char_info[i][0]:
                                char_info[i][1] = new_value.capitalize() # capilizes the class name the user puts in
                        with open(char_file, mode = "w", newline = "") as file:
                            writer = csv.writer(file)
                            writer.writerows(char_info)
                        changes_prompt = input("Any additional changes? y/n: ").lower() #lets the user make additional changes
                        if changes_prompt  == "n":
                            changes = False
                            print("Great changes!")
                            break # breaks inner loop
                        elif changes_prompt == "y":
                            break # loops back through the options
            return
        print("That character does not exist, try again")


# function to print out a csv file the user has selected in view or edit meu options
def print_char(csv_files):
    while True: # loops back if name input is wrong
        char_choice = input("Please enter the name of the character you would like view: ")
        char_file = f"{char_choice}.csv"
        if char_file in csv_files:
            with open(char_file, mode = "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
            break
        else:
            print(f"That character does not exist or you've forgotten missed the capital letter, try again \n")

