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

"""
Problem:
Count the number of vowels and consonants in a string.

Algorithm:
1. Traverse the string.
2. Keep track of vowels and consonants.
3. Increment respective counters based on each character.


Time Complexity:
O(n)

Edge Cases:
- Empty string
- String with all vowels
- String with all consonants

Date Solved:
03 JULY 2026
"""