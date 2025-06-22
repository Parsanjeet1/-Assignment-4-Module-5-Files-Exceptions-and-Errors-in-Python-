# Task 2: Write and append data to a file

file_name = "output.txt"

# Step 1: Write user input to file
user_input = input("Enter some data to write to the file: ")
with open(file_name, "w") as file:
    file.write(user_input + "\n")

# Step 2: Append more data
additional_input = input("Enter additional data to append to the file: ")
with open(file_name, "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display final content
print("\nFinal content of the file:")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
