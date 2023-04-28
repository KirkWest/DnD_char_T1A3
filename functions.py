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
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    print("Select a class from the options below:")
    for i, c in enumerate(classes):
        print(f"{i+1}. {c}")