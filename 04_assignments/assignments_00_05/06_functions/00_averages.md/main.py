def find_average(num1, num2):
    """Returns the average of two numbers."""
    return (num1 + num2) / 2

# Example usage:
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
average = find_average(number1, number2)
print(f"The average of {number1} and {number2} is {average}.")
