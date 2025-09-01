# Write a program to merge two dictionaries.
dict1 = {'tr':32,'z':67}
dict2 = {'a':2,'r':3,'p':6}

print("Original Dictionaries:")
print("dict1 =", dict1)
print("dict2 =", dict2)

merged1 = dict1.copy()
merged1.update(dict2)

print("Merged Dictionary:", merged1)
