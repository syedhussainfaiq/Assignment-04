import random

def guess_my_number():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(1, 99)
    print("I am thinking of a number between 1and 99...")

    while True:
        # Ask the user for their guess
        guess = int(input("Enter a guess: "))
        
        # Compare the guess to the number
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            # If the guess is correct, exit the loop
            print(f"Congrats! The number was: {number_to_guess}")
            break

# Run the game
guess_my_number()
