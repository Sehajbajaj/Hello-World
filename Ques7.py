#Python Program for compound interest
p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

ci =  p * (pow((1 + r / 100), t)) 
print("Compound Interest for the given Principle Amount is: " ,ci)
