# Helper function to subtract 7 from a number
def subtract_seven(num):
    return num - 7

# Main function
def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    # Call subtract_seven with the input number
    result = subtract_seven(num)
    # Print the result
    print(f"{num} minus 7 is {result}")

# Call the main function
main()
