# Write a program to print the Fibonacci series up to n terms.
k = int(input("Enter nth Term = "))
a,b = 0,1
print("Fibonacci series ")
for i in range(k):
    print(a, end = ' ')
    a,b = b,a+b