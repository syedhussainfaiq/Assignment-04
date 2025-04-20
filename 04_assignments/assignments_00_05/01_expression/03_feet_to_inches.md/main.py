def feet_to_inches():
    while True:
        try:
            # Ask the user for input
            feet_input = input("Enter a value in feet (or type 'exit' to quit): ")

            if feet_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Convert the input to a float
            feet = float(feet_input)

            # Calculate the inches
            inches = feet * 12

            # Display the results
            if feet == 1:
                print(f"{feet} foot is equal to {inches} inches.\n")
            else:
                print(f"{feet} feet are equal to {inches} inches.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.\n")

# Run the program
feet_to_inches()
