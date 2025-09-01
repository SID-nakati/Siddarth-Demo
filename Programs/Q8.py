# Write a program to find the largest and smallest number in a list.

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest -> ",max(lst), "  Smallest -> ", min(lst))
