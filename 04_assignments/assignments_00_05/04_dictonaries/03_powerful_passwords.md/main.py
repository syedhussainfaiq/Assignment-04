import hashlib

# Provided hash function (simulated)
def hash_password(password: str) -> str:
    """
    This function hashes the password using SHA256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Sample stored login data (email -> hashed password)
stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("mysecurepassword"),
    "admin@example.com": hash_password("adminpassword")
}

def login(email: str, password_to_check: str) -> bool:
    """
    Checks if the email and password_to_check hash match the stored hash for that email.
    Returns True if they match, False otherwise.
    """
    # Check if the email exists in the stored logins
    if email in stored_logins:
        # Hash the provided password and compare with the stored hashed password
        hashed_password = hash_password(password_to_check)
        return hashed_password == stored_logins[email]
    else:
        # If the email does not exist in the stored logins
        return False

# Test the login function
email = input("Enter your email: ")
password_to_check = input("Enter your password: ")

if login(email, password_to_check):
    print("Login successful!")
else:
    print("Invalid email or password.")
