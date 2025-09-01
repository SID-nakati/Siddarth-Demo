# Write a function to find the second largest number in a list.
k = list(map(int,input("Enter your List with spaces ").split()))
if len(k)<2:
    print("Not enough elements in list")
else:
    print("2nd Largest Number = ",sorted(k)[-2])