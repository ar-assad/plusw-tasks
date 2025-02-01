# Print shape options
print("Calculate the area of following shapes:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

# User input for shape choice (not used for branching)
print("Find the area of Circle: \n")

# Circle area calculation
radius = float(input("Enter the radius of the circle: "))
PI = 3.14159
circle_area = PI * radius * radius  
print("Find the area of Rectangle: \n")

# Rectangle area calculation
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = length * width
print("Find the area of Square: \n")

# Square area calculation
side = float(input("Enter the side length of the square: "))
square_area = side * side
print("Find the area of Triangle: \n")

# Triangle area calculation
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle_area = 0.5 * base * height

# Print all areas
print("All the areas are: \n")
print("The area of the circle is:", circle_area, "\n")
print("The area of the rectangle is:", rectangle_area, "\n")
print("The area of the square is:", square_area, "\n")
print("The area of the triangle is:", triangle_area, "\n")
