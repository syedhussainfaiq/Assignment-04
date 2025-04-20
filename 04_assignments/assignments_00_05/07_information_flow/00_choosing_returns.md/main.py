ADULT_AGE = 18

def is_adult(age):
    """
    Check if a person is an adult based on their age.
    
    Args:
        age: The age of the person to check
        
    Returns:
        bool: True if the person is an adult, False otherwise
    """
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main() 