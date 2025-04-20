MAX_LENGTH: int= 3  # Change this to test with different lengths

def shorten(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed item.
    
    Parameters:
        lst (list): The list to be shortened.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print(f"Removed: {removed_item}")

# Main program
def main():
    user_input = input("Enter a list of items separated by spaces: ")
    lst = user_input.split()  # Create a list from the user input
    print(f"Original list: {lst}")
    
    shorten(lst)
    
    print(f"Shortened list: {lst}")

# Run the program
main()
