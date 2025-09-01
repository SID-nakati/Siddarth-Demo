# Write a program to rotate a list by k positions.
lst = list(map(int,input("Enter your List with spaces ").split()))
p = int(input("Enter the position "))

new = lst[p:] + lst[:p]
print("Qriginal List ",lst)
print("Rotated List  ",new)
