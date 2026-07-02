# today's 1st code
s = "engineering"
vowels = {"a","e", "i", "o", "u"}
vow = []
con = []
for x in s:
    if x in vowels:       
        vow.append(x)      
    else:
        con.append(x)
        
v = len(vow)
c = len(con)
print(f"Number of vowels are {v} ")
print(f"Number of consonants are {c} ")


# today's 2nd code 
s = "chatGPT"
upper = 0
lower = 0
for c in s:
    if c != c.lower():
        upper += 1
    else:
        lower += 1
    
print(upper)
print(lower)