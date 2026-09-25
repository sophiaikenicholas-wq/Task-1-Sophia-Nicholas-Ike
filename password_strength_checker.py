"""
DecodeLabs Cybersecurity Internship - Project 1
Password Strength Checker

This program evaluates a password using:
- Length
- Lowercase letters
- Uppercase letters
- Numbers
- Symbols
- Common/weak password patterns
"""

import string
import getpass

# A small list of commonly used passwords for an extra security check.
COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "qwerty123", "admin", "admin123",
    "letmein", "welcome", "iloveyou"
}


def check_password(password):
    """Return the strength and feedback for a password."""

    length_ok = len(password) >= 8
    uppercase_ok = any(char.isupper() for char in password)
    lowercase_ok = any(char.islower() for char in password)
    number_ok = any(char.isdigit() for char in password)
    symbol_ok = any(char in string.punctuation for char in password)

    # Normalize for comparison with common passwords.
    is_common = password.lower() in COMMON_PASSWORDS

    # Very common/reused-style passwords should not be considered strong.
    if is_common:
        return "Weak", ["This is a commonly used password. Choose something less predictable."]

    checks_passed = sum([
        length_ok,
        uppercase_ok,
        lowercase_ok,
        number_ok,
        symbol_ok
    ])

    feedback = []

    if not length_ok:
        feedback.append("Use at least 8 characters.")
    if not uppercase_ok:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_ok:
        feedback.append("Add at least one lowercase letter.")
    if not number_ok:
        feedback.append("Add at least one number.")
    if not symbol_ok:
        feedback.append("Add at least one symbol.")

    if length_ok and checks_passed >= 5:
        strength = "Strong"
    elif length_ok and checks_passed >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    # getpass prevents the password from being displayed while typed.
    password = getpass.getpass("Enter your password: ")

    strength, feedback = check_password(password)

    print(f"\nPassword Strength: {strength}")

    if strength == "Strong":
        print("Good job! Your password meets all the basic checks.")
    else:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")

    print("\nNote: This checker is an educational tool and does not guarantee")
    print("that a password is impossible to guess or crack.")


if __name__ == "__main__":
    main()
