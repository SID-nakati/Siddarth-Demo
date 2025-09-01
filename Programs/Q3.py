
# Write a program to find the factorial of a number.

n = int(input("Enter the Number = "))
fac = 1
for i in range(1,n+1):
    fac *= i 
print("Factorial is ", fac)