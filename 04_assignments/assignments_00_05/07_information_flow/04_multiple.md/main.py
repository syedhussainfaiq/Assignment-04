# Function to get user data
def get_user_data():
    # Prompt the user for their first name
    first_name = input("What is your first name?: ")
    # Prompt the user for their last name
    last_name = input("What is your last name?: ")
    # Prompt the user for their email address
    email_address = input("What is your email address?: ")
    # Return the data as a tuple
    return first_name, last_name, email_address

# Main function to demonstrate the output
def main():
    # Call get_user_data and store the result
    user_data = get_user_data()
    # Print the received data
    print("Received the following user data:", user_data)

# Call main
main()
