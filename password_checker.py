import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short — use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️  12+ characters makes it much stronger")

    # Character type checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%...)")

    # Common password check
    common_passwords = ["password", "123456", "password123", "admin", "letmein", "qwerty"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("🚨 This is a commonly used password — change it immediately!")

    # Strength rating
    if score <= 2:
        strength = "🔴 WEAK"
    elif score <= 4:
        strength = "🟡 MODERATE"
    elif score == 5:
        strength = "🟢 STRONG"
    else:
        strength = "💪 VERY STRONG"

    return strength, score, feedback


def main():
    print("=" * 45)
    print("       🔐 Password Strength Checker")
    print("=" * 45)

    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")

        if password.lower() == 'quit':
            print("\nStay secure. 👋")
            break

        strength, score, feedback = check_password_strength(password)

        print(f"\nStrength : {strength}")
        print(f"Score    : {score}/6")

        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print(f"  {tip}")
        else:
            print("\n✅ Excellent password! No suggestions.")

        print("-" * 45)


if __name__ == "__main__":
    main()
