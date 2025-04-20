def get_first_element(lst):
    """
    Prints the first element of a non-empty list.
    
    Parameters:
        lst (list): A non-empty list.
    """
    print(f"The first element in the list is: {lst[0]}")

# Main program
n = int(input("Enter the number of elements in the list: "))

# Initialize an empty list
user_list = []

# Prompt the user to input the list elements
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Call the function to get and print the first element
get_first_element(user_list)
