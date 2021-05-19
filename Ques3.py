#Python Program to Calculate the Area of a Triangle, square, and rectangle, circle by taking user input

#Area of triangle
#three sides of triangle are a,b and c
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c) / 2
areat = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("The area Of triangle is %0.2f" %areat)


#Area of square
side = float(input("Enter the side of square: "))
areas = side * side
print("The area of square is %0.2f" %areas)

#Area of rectangle
l = float(input("Enter the length of rectangle: "))
b = float(input("Enter the breadth of rectangle: "))
arear = l * b
print("The area of reactangle is %0.2f" %arear)

#Area of circle
r = float(input("Enter the radius of circle: "))
areac = 3.14 * r * r
print("The area of circle is %0.2f" %areac)
