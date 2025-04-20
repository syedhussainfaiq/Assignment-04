def print_ones_digit(num):
    """
    Print the ones digit of the given number.
    
    Args:
        num (int): The input number
    """
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Get input from user
    number = int(input("Enter a number: "))
    # Call the function to print ones digit
    print_ones_digit(number)

if __name__ == "__main__":
    main() 