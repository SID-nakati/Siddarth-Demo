# Write a program to remove duplicates from a list.
lst = list(map(str,input("Enter your list with spaces ").split()))
print("List Before ->",lst)
k = list(set(lst))
print("List After -> ",k)