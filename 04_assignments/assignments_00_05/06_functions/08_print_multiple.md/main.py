def print_multiple(message, repeats):
    """
    Print a message a specified number of times.
    
    Args:
        message (str): The message to be printed
        repeats (int): The number of times to print the message
    """
    for _ in range(repeats):
        print(message, end=' ')

def main():
    # Get the message from the user
    message = input("Please type a message: ")
    # Get the number of repeats from the user and convert to integer
    repeats = int(input("Enter a number of times to repeat your message: "))
    # Call print_multiple with the user's input
    print_multiple(message, repeats)

if __name__ == "__main__":
    main() 