# Write a program to sort a list without using built-in sort().
k = list(map(int,input("Enter your List with spaces ").split()))

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        l = i
        for j in range(i+1,n):
            if arr[l]>arr[j]:
                l = j
                arr[i],arr[j] = arr[l],arr[i]
    return arr

print("Before Sorting -> ",k)
print("After  Sorting -> ",selection_sort(k))