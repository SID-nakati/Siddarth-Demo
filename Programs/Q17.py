# Write a program to check if two strings are anagrams.
st1 = input("Enter String 1 : ")
st2 = input("Enter String 2 : ")
st1 = st1.replace(" ","").lower()
st2 = st2.replace(" ","").lower()

if sorted(st1)==sorted(st2):
    print("Both strings are Anagrams")
else:
    print("Both are not Anagrams")