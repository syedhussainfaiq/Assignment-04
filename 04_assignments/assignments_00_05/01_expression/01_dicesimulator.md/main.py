import random

def roll_die():
    # This is a local variable
    roll = random.randint(1 , 6)
    return roll

def roll_two_dice():
    # These are also local variables to this function
    die1 = roll_die()
    die2 = roll_die()
    print(f"Rolled: Die 1 = {die1}, Die 2 = {die2}")

    # Main program
for i in range(3):
    print(f"Roll {i + 1}:")
    roll_two_dice () 
