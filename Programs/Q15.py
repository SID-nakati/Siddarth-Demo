# Write a program to find the common elements between two lists.
l1 = list(map(int,input("Enter your List 1 with spaces ").split()))
l2 = list(map(int,input("Enter your List 2 with spaces ").split()))
cmn = []

for i in l1:
    if i in l2 and i not in cmn:
        cmn.append(i)
print("Common Elements are \n ", cmn)
