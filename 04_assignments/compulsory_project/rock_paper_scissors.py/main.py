import random

def who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    
    if (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p"):
        return "You Win!"

    return "You Lose!"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")

    print("Choose 'q' for Quit.")
    
    while True:
        user_choice = input("Enter your choice 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
        
        if user_choice == "q":
            print("Thanks for Playing!")
            break

        if user_choice != "r" and user_choice != "p" and user_choice != "s":
            print("Please Enter a Valid Choice!")
            continue
        
        computer_choice = random.choice(["r", "p", "s"])
        print(f"Computer's Choice: {computer_choice}")
        
        print(who_wins(user_choice, computer_choice))

if __name__ == '__main__':
    main()