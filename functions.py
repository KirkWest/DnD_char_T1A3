def create_menu():
    print("1. To create new character enter 1")
    print("2. To edit previous character enter 2")
    print("3. To see list of created characters enter 3")

# dice roll function, rolls a certain amount of dice to be specified then removes the
# lowest number as per DnD rules (usually 4 die, so only count the top 3 scores count)
def dice_roll(num_dice):
    import random
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, 6))
    rolls.remove(min(rolls))

# character name input def
def char_name():
    name = input("What name would you like to call your character?: ")
    return name

# list of classes available
def print_classes():
    print("1. Barbarian")
    print("2. Bard")
    print("3. Cleric")
    print("4. Druid")
    print("5. Fighter")
    print("6. Monk")
    print("7. Paladin")
    print("8. Ranger")
    print("9. Rogue")
    print("10. Sorcerer")
    print("11. Warlock")
    print("12. Wizard")
    choice = input("Which class would you like? press '1-12' to select")
    return choice