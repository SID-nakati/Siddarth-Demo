# Write a function that accepts **kwargs and returns the sum of values.
def summ(**k):
    return sum(k.values())
res = summ(a=10,b=54,t=32)
print(res)
