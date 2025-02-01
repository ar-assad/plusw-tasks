import random

# List of colors
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# Generate a random index
index = random.randint(0, len(colors) - 1)

# Select the color
selected_color = colors[index]

# Reverse the selected color for the password
password = selected_color[::-1]

# Print the results
print("Selected Color:", selected_color)
print("Generated Password:", password)
