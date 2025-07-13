# 🔐 Password Generator Script

import random
import string

def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters  # A–Z and a–z

    if use_digits:
        characters += string.digits  # 0–9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&*() etc.

    if length < 4:
        return "❌ Password too short. Use at least 4 characters."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Strong Password Generator\n")

    try:
        length = int(input("Enter desired password length (e.g. 12): "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_digits, include_symbols)
    print(f"\n✅ Your generated password: {password}")

    # Save to file
    with open("generated_password.txt", "a") as file:
        file.write(password + "\n")
    print("💾 Password saved to 'generated_password.txt'.")

if __name__ == "__main__":
    main()