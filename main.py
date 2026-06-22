import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    ratings = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return ratings[score], feedback


password = input("Enter a password to analyze: ")

rating, tips = check_password_strength(password)

print("\nPassword Strength:", rating)

if tips:
    print("\nSuggestions:")
    for tip in tips:
        print("-", tip)
