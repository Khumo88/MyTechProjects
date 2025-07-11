def calculate_password_strength(password):
    score = 0

    # 1. Length Check
    if len(password) >= 8:
        score += 3
    elif len(password) >= 5:
        score += 1

    # 2. Contains number
    if any(char.isdigit() for char in password):
        score += 2

    # 3. Contains special character
    if any(not char.isalnum() for char in password):
        score += 2

    # 4. Contains both uppercase and lowercase
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 3

    return min(score, 10) # Max out at 10

def password_strength_messsage(score):
    if score >= 8:
        return "✅ Very Strong Password!"
    elif score >+ 5:
        return "⚠️ Medium Strength Password. Improve it."
    else:
        return "❌ Weak Password. Change it now!"
    
# 🧪 Test the function
password = input("Enter your paasword:")
score = calculate_password_strength(password)
print(f"\n🔐 Password score: {score}/10")
print(password_strength_messsage(score))