#WAP that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))
year = int(input("Enter the Present Year: "))
print(name)
print(age)
t = 100 - age
ans = year + t
print("You will turn 100 in the year ",ans,"")
