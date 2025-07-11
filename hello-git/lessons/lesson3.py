# Lesson 3- if statements and for loops
# Ask the user for their age
age = int(input("Enter your age: "))

# Check if user is adult or minor
if age >= 18:
    print("You are an adult.")
else:
    print("You ar a minor.")
   
 # Loop to print numbers from 1 to 5
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("Done with lesson 3.")