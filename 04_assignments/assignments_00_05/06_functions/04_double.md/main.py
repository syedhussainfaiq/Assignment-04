def double(num):
    """Returns the result of multiplying num by 2."""
    return num * 2

def main():
    """Prompts the user for a number and prints its double."""
    try:
        num = float(input("Enter a number: "))
        result = double(num)
        print(f"Double that is {result}")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()
