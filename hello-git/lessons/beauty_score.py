import random

def calculate_beauty_score(name):
    score = random.randint(60, 100)
    print(f"\n{name}, your beauty score is: {score}% 💅🏼")

# Ask for a name
name = input("Enter your name:")
while name.strip() == "":
    name = input("Name cannot be empty. Enter your name:")

calculate_beauty_score(name)