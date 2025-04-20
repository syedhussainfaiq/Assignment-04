def count_numbers():
    """
    Continuously asks the user to input numbers and counts how many times each number appears.
    """
    number_count = {}  # Dictionary to store the count of each number
    
    while True:
        # Prompt the user for a number
        number = input("Enter a number: ")
        
        # If the input is empty, break the loop
        if number == "":
            break
        
        # Convert input to an integer
        number = int(number)
        
        # Update the count of the number in the dictionary
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1
    
    # Print the count of each number in the dictionary
    for number, count in number_count.items():
        print(f"{number} appears {count} times.")

# Run the function
count_numbers()
