def phonebook():
    """
    A simple phonebook program using a dictionary to store names and phone numbers.
    """
    phonebook_dict = {}  # Dictionary to store phonebook entries
    
    while True:
        # Prompt the user for a choice
        print("\nPhonebook Options:")
        print("1. Add contact")
        print("2. Lookup contact")
        print("3. Exit")
        
        choice = input("Choose an option (1, 2, or 3): ")
        
        if choice == '1':
            # Add a contact
            name = input("Enter the name of the contact: ")
            phone_number = input(f"Enter the phone number for {name}: ")
            phonebook_dict[name] = phone_number
            print(f"{name} added to the phonebook.")
        
        elif choice == '2':
            # Lookup a contact
            name = input("Enter the name of the contact to lookup: ")
            if name in phonebook_dict:
                print(f"{name}'s phone number is {phonebook_dict[name]}.")
            else:
                print(f"{name} not found in the phonebook.")
        
        elif choice == '3':
            # Exit the program
            print("Exiting the phonebook.")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the phonebook function
phonebook()
