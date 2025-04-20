def fruit_shop():
    """
    A program to calculate the total cost of fruits based on user input.
    """
    # Dictionary containing fruit names and their prices
    fruit_prices = {
        "apple": 2.5,
        "durian": 5.0,
        "jackfruit": 3.0,
        "kiwi": 4.0,
        "rambutan": 2.0,
        "mango": 3.5
    }
    
    total_cost = 0  # Initialize the total cost
    
    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        # Ask the user how many of each fruit they want
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price  # Add the cost of the fruit to the total
    
    # Print the total cost
    print(f"Your total is ${total_cost:.1f}")

# Run the fruit shop function
fruit_shop()
