import math

def calculate_hypotenuse():
    while True:
        try:
            # Prompt the user for the lengths of the two sides
            ab_input = input("Enter the length of AB (or type 'exit' to quit): ")
            if ab_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            ac_input = input("Enter the length of AC (or type 'exit' to quit): ")
            if ac_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Convert the inputs to floats
            ab = float(ab_input)
            ac = float(ac_input)

            # Calculate the hypotenuse using the Pythagorean theorem
            bc = math.sqrt(ab**2 + ac**2)

            # Output the result
            print(f"\nThe length of BC (the hypotenuse) is: {bc}\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers or type 'exit' to quit.\n")

# Run the program
calculate_hypotenuse()
