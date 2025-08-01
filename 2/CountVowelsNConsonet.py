vowels=['e', 'a', 'i', 'o', 'u', 'E', 'A', 'I', 'O', 'U']

string=input()
v_c=0
c_c=0
for i in string:
    if i in vowels:
        v_c+=1
    if i not in vowels and i.isalpha():
        c_c+=1
        
print("Vowels:", v_c)
print("Consonants:", c_c)