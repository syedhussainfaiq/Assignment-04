def collect_values():
    """
    Continuously prompts the user to enter values and adds them to a list.
    Stops when the user presses Enter without typing anything, and prints the list.
    """
    values = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        values.append(value)
    
    print(f"Here's the list: {values}")

# Run the program
collect_values()
