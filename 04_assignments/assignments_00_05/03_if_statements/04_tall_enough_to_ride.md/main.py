def check_leap_year(year):
    """
    Checks whether the given year is a leap year based on the Gregorian calendar rules.
    
    Parameters:
        year (int): The year to be checked.
    """
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, it's not a leap year unless it's also divisible by 400
        if year % 100 == 0:
            # Divisible by 400 means it's a leap year
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Main program
year = int(input("Enter a year: "))
check_leap_year(year)
