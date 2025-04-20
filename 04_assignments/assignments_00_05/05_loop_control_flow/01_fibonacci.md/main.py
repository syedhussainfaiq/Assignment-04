# Define the maximum value as a constant
MAX_VALUE = 10000

def generate_fibonacci(max_value):
    # Initialize the first two terms
    a, b = 0, 1
    
    # Print terms of the Fibonacci sequence
    while a < max_value:
        print(a, end=" ")  # Print the current term
        a, b = b, a + b  # Update terms

# Run the function
generate_fibonacci(MAX_VALUE)
