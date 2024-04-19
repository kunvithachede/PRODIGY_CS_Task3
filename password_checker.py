import re

def check_password_strength(password):
    length_score = min(len(password) / 8, 1)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    letter_score = int(has_upper and has_lower)
    has_number = any(c.isdigit() for c in password)
    number_score = int(has_number)
    has_special = bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', password))
    special_score = int(has_special)
    total_score = (length_score + letter_score + number_score + special_score) / 4
    if total_score >= 0.75:
        return "Strong password"
    elif total_score >= 0.5:
        return "Moderate password"
    elif total_score >= 0.25:
        return "Weak password"
    else:
        return "Very weak password"

password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
