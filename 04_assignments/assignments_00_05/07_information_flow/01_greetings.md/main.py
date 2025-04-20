def greet(name):
    """Print a greeting for the given name."""
    print(f"Greetings {name}!")

def main():
    # Get the user's name
    name = input("What's your name? ")
    
    # Call the greet helper function
    greet(name)

if __name__ == "__main__":
    main() 