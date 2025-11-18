import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    """
    Generates a random password based on specified criteria.
    
    Parameters:
    - length (int): The desired length of the password (default: 12).
    - include_uppercase (bool): Include uppercase letters (default: True).
    - include_lowercase (bool): Include lowercase letters (default: True).
    - include_digits (bool): Include digits (default: True).
    - include_symbols (bool): Include special symbols (default: True).
    
    Returns:
    - str: The generated password.
    """
    # Build the character pool based on options
    char_pool = ""
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation
    
    # Ensure at least one character type is selected
    if not char_pool:
        raise ValueError("At least one character type must be included.")
    
    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    # Generate a default 12-character password with all types
    print("Generated password:", generate_password())
    
    # Customize: 16 characters, no symbols
    print("Custom password (16 chars, no symbols):", generate_password(length=16, include_symbols=False))
