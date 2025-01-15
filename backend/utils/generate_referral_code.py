import random
import string

def generate_referral_code():
    # Generate 3 random uppercase letters
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    # Generate 3 random digits
    digits = ''.join(random.choices(string.digits, k=3))
    # Generate 1 random lowercase letter
    lowercase_letter = random.choice(string.ascii_lowercase)
    # Combine them in the format ABC123x
    code = f"{letters}{digits}{lowercase_letter}"
    return code

# Example usage
print(generate_referral_code())