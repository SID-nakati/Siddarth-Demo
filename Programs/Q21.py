# Write a program to implement binary search.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found
k = list(map(int,input("Enter your List with spaces ").split()))
k.sort()
t = int(input("Enter Target to be found = "))
print("Target Index is ->", binary_search(k,t))