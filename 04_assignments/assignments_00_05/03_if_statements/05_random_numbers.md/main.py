import random

def print_random_numbers():
    """
    Prints 10 random numbers in the range from 1 to 100.
    """
    for _ in range(10):  # Repeat the process 10 times
        print(random.randint(1, 100), end=" ")  # Generate a random number and print it on the same line

# Call the function to print the random numbers
print_random_numbers()
