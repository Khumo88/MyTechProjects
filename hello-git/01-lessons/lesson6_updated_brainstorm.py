# lesson6.py - Lists and Loops

print("Welcome to Lesson 6: Lists and Loops\n")

# A list of tech topics
topic = ["Python", "Cybersecurity", "Git", "Linux",]

# Display the list using a Loop
print("Here are some tech topics:")
for t in topic:
    print("_" + t)

# Ask the user to add another topic
new_topic = input("\nWhat tech topic would you like to add?")

# Add it to the list
topic.append(new_topic)

# Show updated list
print("\nUpdated list of topics:")
for t in topic:
    print("_ " + t)