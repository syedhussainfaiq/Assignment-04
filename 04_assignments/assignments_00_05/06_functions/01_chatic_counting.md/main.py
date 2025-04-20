import random

# Define the likelihood of stopping
DONE_LIKELIHOOD = 0.2

def done():
    """Returns True with a likelihood of DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Prints numbers from 1 to 10 but stops early if done() returns True."""
    for i in range(1, 11):  # Loop from 1 to 10
        if done():
            return  # Exit the function if done() returns True
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Run the main function
main()
