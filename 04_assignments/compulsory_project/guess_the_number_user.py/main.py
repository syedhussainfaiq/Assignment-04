import random

def main(x):    
    print(f"Please Guess a number between 1 and {x}...")
    low = 1
    high = x
    feedback = ''

    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} is too high(h), too low(l) or correct(c):")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            break
        else:
            print("Please Enter a Valid Input!")
        if low == high:
            guess = low
            break

        
    print(f"Computer Guessed the correct number, The number was: {str(guess)}")
    
if __name__ == '__main__':
    main(99)