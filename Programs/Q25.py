# Write a program to find the longest word in a given sentence.
st = input("Enter the sentence \n")
word = st.split(" ")
m = 0
index = 0
for i in range(len(word)):
    if len(word[i])>m:
        m = len(word[i])
        index = i
print("The longest word in the sentence is \n",word[index])