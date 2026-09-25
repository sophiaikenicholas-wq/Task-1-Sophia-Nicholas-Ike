import re

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters required).")

    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 4. Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one numeric digit (0-9).")

    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    # Common weak passwords blacklist
    common_passwords = ["password", "123456", "12345678", "qwerty", "admin", "password123"]
    if password.lower() in common_passwords:
        return "Very Weak", ["This is a extremely common leaked password. Choose something unique."]

    # Strength Classification
    if score >= 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

# Example Usage
if __name__ == "__main__":
    user_pass = input("Enter a password to test: ")
    strength, suggestions = check_password_strength(user_pass)
    
    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions for improvement:")
        for note in suggestions:
            print(f"- {note}")