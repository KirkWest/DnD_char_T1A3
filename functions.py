def create_menu():
    print("1. Create new character enter 1")
    print("2. Edit previous character enter 2")
    print("3. See list of created characters enter 3")
    print("4. Exit enter 4")
    menu_choice = input("Type the number (1-4): ")
    return menu_choice
    

# character name input def
def char_name():
    name = input("What name would you like to call your character?: ")
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
    import random
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, 6))
    rolls.remove(min(rolls))
    return sum(rolls)


