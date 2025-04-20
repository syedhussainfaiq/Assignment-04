def count_even():
    """Prompts the user for integers and counts how many are even."""
    lst = []
    
    # Prompt user for input until they press enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")

    # Count even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    
    print(f"The number of even numbers in the list is: {even_count}")

# Run the function
count_even()
