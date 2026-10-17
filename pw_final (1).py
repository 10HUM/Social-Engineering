# Final Script: Password Strength Checker

import re

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "123456789", "letmein", "iloveyou",
    "admin", "welcome", "monkey", "football", "dragon"
]


def check_length(password):
    """Check the password length."""
    if len(password) >= 8:
        return True, "Length: OK (8+ characters)."
    else:
        return False, "Length: Weak. Use at least 8 characters."


def check_case(password):
    """Check for uppercase and lowercase letters."""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if has_upper and has_lower:
        return True, "Case: OK (contains upper and lowercase letters)."
    else:
        return False, "Case: Weak. Include both uppercase and lowercase letters."


def check_numbers_special(password):
    """Check for numbers and special characters."""
    has_number = any(char.isdigit() for char in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    if has_number and has_special:
        return True, "Numbers/Special: OK (contains numbers and special characters)."
    else:
        return False, "Numbers/Special: Weak. Include at least one number and one special character."


def check_common_passwords(password):
    """Check if the password is a commonly used password."""
    if password.lower() in COMMON_PASSWORDS:
        return False, "Common Password: Weak. This password is too common."
    else:
        return True, "Common Password: OK (not a common password)."


def check_password_strength(password):
    """Evaluates the password using all checks and returns feedback."""
    results = []

    # Call each function and collect feedback
    length_ok, length_msg = check_length(password)
    case_ok, case_msg = check_case(password)
    num_spec_ok, num_spec_msg = check_numbers_special(password)
    common_ok, common_msg = check_common_passwords(password)

    results.append(length_msg)
    results.append(case_msg)
    results.append(num_spec_msg)
    results.append(common_msg)

    # Determine overall strength
    if all([length_ok, case_ok, num_spec_ok, common_ok]):
        return "Strong password! Good job."
    else:
        return "Weak password. Recommendations:\n" + "\n".join(results)


# Get user input and validate it
password = input("Enter a password to check its strength: ")

while not password:
    password = input("You did not enter a password. Please enter a password: ")

# Call the function and display the results
print(check_password_strength(password))
