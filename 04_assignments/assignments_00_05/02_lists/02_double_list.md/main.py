def double_numbers(numbers):
    """
    Takes a list of numbers and doubles each element.
    
    Parameters:
        numbers (list): A list of numerical values.
    
    Returns:
        list: A new list with each number doubled.
    """
    return [number * 2 for number in numbers]

# Example usage:
numbers = [1, 2, 3, 4]
doubled_numbers = double_numbers(numbers)
print(f"Original list: {numbers}")
print(f"Doubled list: {doubled_numbers}")
