#WAP to get user input of 5 numbers to find the average of the number and calculate percentage.

num1 = float(input("no1: "))
num2 = float(input("no2: "))
num3 = float(input("no3: "))
num4 = float(input("no4: "))
num5 = float(input("no5: "))
avg = (num1 + num2 + num3 + num4 + num5) / 5
percentage = (num1 + num2 + num3 + num4 + num5) / 500 * 100
print("The average of numbers: %0.2f" %avg)
print("The percentage of number: %0.2f" %percentage)

