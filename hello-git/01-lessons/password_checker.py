def check_password_strength(password):
    length_ok = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if length_ok and has_number and has_special:
        print("✅ Strong password!")
    elif length_ok:
        print("⚠️ Medium password. Try adding numbers or special characters.")
    else:
        print("❌ Weak password. Must be at least 8 characters.")

# Get user input
password = input("Enter your password to check: ")
check_password_strength(password)