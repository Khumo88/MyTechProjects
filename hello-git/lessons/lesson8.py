# lesson8_file_handling.pu

print("Welcome to Lesson 8: File Handling (Read/Write Text Files)")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("We are learning how to read and write files in Python.\n")

print("Data written to example.txt successfully.\n")

# Reading the entire file content
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content (read all):")
    print(content)

# Appending to the file
with open("example.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("Data appended to example.txt successfully.\n")

# Reading the file line by line
print("Reading file line by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n🎉 Lesson 8 Complete! You have learned how to read and write files in Python.")