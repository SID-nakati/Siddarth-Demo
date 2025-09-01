#Write a program to swap two numbers without using a third variable.

a = int(input("Enter first number ="))
b = int(input("Enter second number ="))

''' a = 5 b =1 0
    a = a+b    a = 15
    b = a-b    b = 5
    a = a-b    a = 10'''
print("Before swapping  a ->", a , " b-> " ,b )
a,b = b,a

print("After swapping   a ->", a , "  b-> " ,b )
