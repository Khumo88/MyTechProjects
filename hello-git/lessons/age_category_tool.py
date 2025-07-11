# 🔢 Ask for the user's age
age_input = input("Please enter your age: ")

# ✅ Validate that it's a number
if age_input.isdigit():
    age = int(age_input)

    # 🧠 Determine the category
    if age < 0:
        print("Age cannot be negaative.")
    elif age <= 12:
        print("You are a Child 👶🏽")
    elif age <= 19:
        print("You are a Teenager 👧🏽")
    elif age <= 59:
        print("You are a Adult 👩🏽")
    else:
        print("You are a Senior 👵🏽")

else:
    print("Invalid input. Pkease enter a numeric age.")