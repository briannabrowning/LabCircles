# calc a circle's diameter, circumfrence and area

# When the user enters valid data, create an instance of a Circle
# then use its methods to display the Diameter, Circumference and Area.
import math



# create a class named Circle to store the data about the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def diameter(self):
        diameter = self.radius * 2
        return diameter
    def circumference(self):
        circumference = self.radius * math.pi * 2
        return circumference
    def area(self):
        area = (self.radius ** 2) * math.pi
        return area
    def grow(self):
        self.radius *= 2

# loop to get valid radius from user
print("Welcome to the circle tester.")
while True:
    # prompt user to enter a radius (may use decimals - float)
    try:
        radius = float(input('Enter a radius: '))
        break             # cant return bc then the function would exit
    # confirm valid data & display error
    except ValueError:
        radius = float(input('Enter a valid number: '))

# create an instance of circle
circle = Circle(radius)

# print the calculations
print(f"Diameter: {circle.diameter()}")
print(f"Circumference: {circle.circumference()}")
print(f"Area: {circle.area()}")


# ask if the circle should grow
choice = input("Do you want the circle to grow? y/n ")
while True:
    if choice == "y":
        # call grow method (double radius) & loop back to the method calls for formulas
        circle.grow()
        print(f"New radius: {circle.radius}")
        print(f"New diameter: {circle.diameter()}")
        print(f"New circumference: {circle.circumference()}")
        print(f"New area: {circle.area()}")
    else:
        print("Goodbye")