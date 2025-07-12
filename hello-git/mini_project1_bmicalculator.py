# 🧮 MINI-PROJECT 1: BMI CALCULATOR

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_result_to_file(name, age, bmi, category):
    with open("bmi_results.txt", "a") as file:
        file.write(f"{name}, Age: {age}, BMI: {bmi:.2f}, Category: {category}\n")

def main():
    print("📏 Welcome to the BMI Calculator!\n")
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    try:
        height = float(input("Enter your height in meters (e.g. 1.65): "))
        weight = float(input("Enter your weight in kilograms (e.g. 68): "))
    except ValueError:
        print("❌ Please enter valid numbers for height and weight.")
        return

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"\n✅ Hello {name}, age {age}.")
    print(f"Your BMI is {bmi:.2f} — Category: {category}")

    save_result_to_file(name, age, bmi, category)
    print("\n💾 Your result has been saved to 'bmi_results.txt'.")

if __name__ == "__main__":
    main()