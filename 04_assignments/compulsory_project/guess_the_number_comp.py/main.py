import random

def main(x):
    secret_number = random.randint(1, x)
    
    print(f"I am thinking of a number between 1 and {x}...")
    
    while True:
        guess = input("Enter a guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess < 1 or guess > 99:
                print("Please Enter a Valid Number!") 
            else:
                break
        else:
            print("Please Enter a Valid Number!") 

    while guess != secret_number:
        if guess < secret_number: 
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        while True:
            guess = input("Enter a guess: ")
            if guess.isdigit():
                guess = int(guess)
                if guess < 1 or guess > 99:
                    print("Please Enter a Valid Number!")
                else:
                    break
            else:
                print("Please Enter a Valid Number!") 
        
    print(f"Congrats! The number was: {str(secret_number)}")
    
if __name__ == '__main__':
    main(99)