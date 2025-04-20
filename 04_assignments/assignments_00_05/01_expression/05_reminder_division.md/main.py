def division_with_remainder():
    while True:
        try:
            # Prompt the user for the first number
            num1_input = input("Please enter an integer to be divided (or type 'exit' to quit): ")
            if num1_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Convert the input to an integer
            num1 = int(num1_input)

            # Prompt the user for the second number
            num2_input = input("Please enter an integer to divide by (or type 'exit' to quit): ")
            if num2_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Convert the input to an integer
            num2 = int(num2_input)

            # Perform division and calculate the remainder
            quotient = num1 // num2
            remainder = num1 % num2

            # Output the result
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}\n")
        except ValueError:
            print("Invalid input. Please enter valid integers or type 'exit' to quit.\n")
        except ZeroDivisionError:
            print("Division by zero is not allowed. Please try again.\n")

# Run the program
division_with_remainder()
