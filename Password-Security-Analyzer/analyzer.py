import re
from config import COMMON_PASSWORDS, MIN_PASSWORD_LENGTH


def analyze_password(password):
    """
    Analyze password strength and return detailed results.
    """

    score = 0
    suggestions = []

    # Empty password
    if not password:
        return {
            "score": 0,
            "strength": "No Password",
            "suggestions": ["Enter a password to analyze"],
            "length": 0
        }

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        return {
            "score": 0,
            "strength": "Very Weak",
            "suggestions": [
                "This is a commonly used password",
                "Choose a unique password"
            ],
            "length": len(password)
        }

    # Password length
    if len(password) >= MIN_PASSWORD_LENGTH:
        score += 1
    else:
        suggestions.append(
            f"Use at least {MIN_PASSWORD_LENGTH} characters"
        )

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter"
        )

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter"
        )

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one number"
        )

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one special character"
        )

    # Strength classification
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # If no suggestions
    if not suggestions:
        suggestions.append(
            "Excellent password structure"
        )

    return {
        "score": score,
        "strength": strength,
        "suggestions": suggestions,
        "length": len(password)
    }