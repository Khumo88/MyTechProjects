# Lesson 4 - While Looops and Input Validation

# Ask for a name until the user types something valid
name = input("What is your name?")
while name.strip() == "":
    print("Name can't be empty. Try again.")
    name = input("What is your name?")

# Ask for age and make sure it's a positive number
age = input("What is your age?")
while not age.isdigit() or int(age) <= 0:
    print("Please enter a valid positive number.")
    age = input("What is your age?")

# Print result
print("\nWelcome,", name + "!")
print("You are", age, "years old.")