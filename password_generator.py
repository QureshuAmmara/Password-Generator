import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    if length < (use_upper + use_lower + use_numbers + use_symbols):
        return "Password length is too short for the selected character sets."

    char_pool = []
    password = []
    
    # Ensure at least one of each selected type
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
        char_pool.extend(string.ascii_uppercase)
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
        char_pool.extend(string.ascii_lowercase)
    if use_numbers:
        password.append(random.choice(string.digits))
        char_pool.extend(string.digits)
    if use_symbols:
        password.append(random.choice(string.punctuation))
        char_pool.extend(string.punctuation)

    # Fill in the rest of the password length
    password += random.choices(char_pool, k=length - len(password))

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
print(generate_password(12, True, True, True, True))