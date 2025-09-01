# Write a program to count vowels and consonants in a string.
st = input("Enter your string \n")
vow = 'aeiouAEIOU'
st = st.replace(" ","")
print(st)
c_cnt = v_cnt = 0
for i in st.strip(" "):
    if i in vow:
        v_cnt += 1
    else:
        c_cnt += 1
print(f"Vowels -> {v_cnt}  Consonants -> {c_cnt} ")
