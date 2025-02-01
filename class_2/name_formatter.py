# Input first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Convert first name to uppercase and last name to lowercase
first_name = first_name.upper()
last_name = last_name.lower()

# Calculate and print the sum of the letters
total_letters = len(first_name) + len(last_name)

# Print the formatted output
print(f"First name (upper): {first_name}")
print(f"Last name (lower): {last_name}")
print("Sum of letters in your first and last name:", total_letters)
