import random

def main():
    print("Welcome to the Password Generator!")

    while True:
        password_qty = input("How many Passwords do you want: ")
        if password_qty.isdigit():
            password_qty = int(password_qty)
            break
        else:
            print("Please enter a valid number.")

    while True:
        password_length = input("Please enter the length of the password: ")
        if password_length.isdigit():
            password_length = int(password_length)
            break
        else:
            print("Please enter a valid number.")
    
    print("Your PasswordS:")

    for i in range(password_qty):
        password = ""
        for _ in range(password_length):
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
        print(f"{i+1}. {password}")
    
    print("Password Generation Completed!")

if __name__ == "__main__":
    main()