# Write a program to check if a string is a palindrome.
def ispalindrome(s):
    return s == s[::-1]
st = input("Enter your string \n")

print("Palindrome " if ispalindrome(st) else "Not a Palindrome")