import random

def roll_die():
    """Simulates rolling a single six-sided die."""
    return random.randint(1, 6)

def roll_two_dice():
    """Rolls two dice and returns their individual results and total."""
    die1 = roll_die()
    die2 = roll_die()
    total = die1 + die2
    return die1, die2, total

def display_results(die1, die2, total):
    """Displays the results of the dice rolls."""
    print(f"\nYou rolled a {die1} and a {die2}.")
    print(f"The total is {total}.\n")

def ask_to_roll_again():
    """Asks the user if they want to roll again."""
    while True:
        response = input("Would you like to roll again? (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("Please answer 'yes' or 'no'.")

def main():
    """Main function to run the dice rolling simulation."""
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        die1, die2, total = roll_two_dice()
        display_results(die1, die2, total)
        if not ask_to_roll_again():
            print("Thanks for playing! Goodbye!")
            break

# Run the program
main()
