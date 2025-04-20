# Function simulating Sophia's inventory
def num_in_stock(fruit):
    # Inventory dictionary
    inventory = {
        "apple": 50,
        "banana": 100,
        "pear": 1000,
        "orange": 75,
        "grape": 200,
    }
    # Return the count of the fruit, or 0 if not found
    return inventory.get(fruit.lower(), 0)

# Main function
def main():
    # Prompt user for a fruit
    fruit = input("Enter a fruit: ")
    # Get the number in stock
    stock_count = num_in_stock(fruit)
    
    if stock_count > 0:
        print(f"This fruit is in stock! Here is how many:\n{stock_count}")
    else:
        print("This fruit is not in stock.")

# Call main
main()
