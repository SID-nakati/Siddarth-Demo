# Write a program to read command-line arguments using sys.argv.
 
import sys
tot=0
k=len(sys.argv)

print("Code Executed -> ",sys.argv[0])
print("Number Of Arguments ->" , k-1)
print("Argument Read ")
for i in range(1,k):
    print(sys.argv[i],end=" ")
 
