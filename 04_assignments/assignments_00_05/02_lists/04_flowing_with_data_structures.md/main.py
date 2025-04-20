def add_three_copies(data_list, data):
    """
    Adds three copies of the given data to the list.
    
    Parameters:
        data_list (list): The list to which data is added.
        data: The data to be added to the list.
    """
    for _ in range(3):
        data_list.append(data)

# Main program
message = input("Enter a message to copy: ").strip()

# Initialize an empty list
my_list = []

# Display the list before modification
print(f"List before: {my_list}")

# Call the function to add three copies
add_three_copies(my_list, message)

# Display the list after modification
print(f"List after: {my_list}")
