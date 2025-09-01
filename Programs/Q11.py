
# Write a program to count the frequency of each element in a list.

lst = list(map(str,input("Enter your list elements with spaces \n").split(" ")))
cnt = dict()
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else :
        cnt[i]=1
for i,j in cnt.items():
    print(i, "->", j)