import math

print("Calculate the area of the following shapes:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

shape = input("Enter the number corresponding to the shape: ")

if shape == "1":
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f}")

elif shape == "2":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")

elif shape == "3":
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area:.2f}")

elif shape == "4":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}")

else:
    print("Invalid choice! Please enter a valid number (1-4).")
