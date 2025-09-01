# Write a program to find all prime numbers in a given range.

def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def prime(sr,en):
    return [i for i in range(sr,en) if isprime(i)]

st = int(input("Enter Start = "))
en = int(input("Enter End   = "))
print("Prime Number between",st,'and',en,'are\n',prime(st,en))