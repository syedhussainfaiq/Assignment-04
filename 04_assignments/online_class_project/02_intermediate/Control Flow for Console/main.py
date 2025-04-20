import random

def play_high_low_game(rounds=5):
    """
    Play the High-Low game for a specified number of rounds.
    
    Args:
        rounds (int): Number of rounds to play (default: 5)
    """
    player_score = 0
    
    print("Welcome to the High-Low Game!")
    print(f"You will play {rounds} rounds. In each round:")
    print("1. You and the computer will each get a random number from 1 to 100")
    print("2. You'll see your number but not the computer's")
    print("3. Guess if your number is higher or lower than the computer's")
    print("4. Get a point if your guess is correct!\n")
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        
        # Generate random numbers
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is: {player_number}")
        
        # Get player's guess
        while True:
            guess = input("Is your number higher or lower than the computer's? (h/l): ").lower()
            if guess in ['h', 'l']:
                break
            print("Please enter 'h' for higher or 'l' for lower.")
        
        # Determine if guess is correct
        is_higher = player_number > computer_number
        is_correct = (guess == 'h' and is_higher) or (guess == 'l' and not is_higher)
        
        # Show results
        print(f"Computer's number was: {computer_number}")
        if is_correct:
            player_score += 1
            print("Correct! You get a point!")
        else:
            print("Incorrect! No point this round.")
        
        print(f"Current score: {player_score}/{round_num}")
    
    # Game summary
    print("\nGame Over!")
    print(f"Final score: {player_score}/{rounds}")
    print(f"Win percentage: {(player_score/rounds)*100:.1f}%")

if __name__ == "__main__":
    play_high_low_game() 