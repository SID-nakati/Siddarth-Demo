# Write a program to count the number of words in a text file.
file = open("text.txt",'r')
content = file.read()
file.close()
words = content.split(" ")
print("Number of words are = ",len(words))