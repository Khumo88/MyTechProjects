# lesson7.py
# Lesson 7: Dictionaries and Functions in Python

# --- Dictionaries ---
# A dictionary stores data in key-value pairs.

# Example dictionary about a person
person = {
    "name": "Khumo",
    "age": 37,
    "course": "Cybersecurity"
}

# Accessing dictionary values by key
print("Name:", person["name"])      # Output: Khumo
print("Age:", person["age"])        # Output: 37
print("Course:", person["course"])  # Output: Cybersecurity

# Adding a new key-value pair
person["city"] = "Mafikeng"
print("City added:", person["city"])  # Output: Mafikeng

# Updating an existing key's value
person["age"] = 38
print("Updated Age:", person["age"])  # Output: 38

# Looping through dictionary keys and values
print("\nAll person details:")
for key, value in person.items():
    print(f"{key}: {value}")

# --- Functions ---
# Functions help you reuse blocks of code.

# Define a function to greet a person by name
def greet(name):
    print(f"\nHello, {name}! Welcome to Lesson 7.")

# Call the function with a value
greet(person["name"])

# Define a function that adds two numbers and returns the result
def add_numbers(a, b):
    return a + b

# Call the function and store the result
result = add_numbers(10, 5)
print(f"\n10 + 5 = {result}")

# Another example: Function with default parameters
def describe_course(name="Student", course="Python"):
    print(f"\n{name} is learning {course}.")

describe_course()                  # Uses default values
describe_course("Khumo", "Cybersecurity")  # Custom values