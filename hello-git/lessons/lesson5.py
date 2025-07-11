# Lesson 5 - Intro to Functions

# Define a function to greet the user
from os import name


def greet_user(name, age):
    print(f"\nHello, {name}!")
    print(f"You are {age} years old.")
    print("Welcome to Lesson 5 - Functions!")

# Define a function to check if the user is an adult
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

# Ask for valid name
name = input("What is your name? ")
while name.strip() == "":
    print("Name can't be empty. Please enter your name.")
    name = input("What is your name? ")
    
# Ask for valid age
age_input = input("Enter your age: ")
while not age_input.isdigit() or int(age_input) <= 0:
    print("Invalid age. Please try again.")
    age_input = input("Enter your age: ")
age = int(age_input)

# Call the functions
greet_user(name, age)

if is_adult(age):
    print("You're an adult.")
else:
    print("You're still a minor.")

print("Done with Lesson 5!")