# Speed of light in metres per second

C: int = 299792458


def main():
    while True:
        try:

            #Ask the user for mass input
            mass_input = input("Enter kilos of mass  (or type 'exit' to quit):")


            if mass_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Convert mass input to float
            mass = float(mass_input)

            # Calculate the energy using Einstein's formula
            energy = mass * C** 2

            # Display the result
            print("\nE = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f" {energy} joules of energy!\n")

        except ValueError:
            print ("Invalid input. Please enter a valid number or type 'exit to quit.\n" )

if __name__ == '__main__':
    main()