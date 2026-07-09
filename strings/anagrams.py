def are_anagrams(s, s2):
    
    if len(s) != len(s2):
        return False
        
    freq = {}
    q = {}
    
  
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
     
   
    for ch in s2:
        if ch in q:
            q[ch] += 1
        else:
            q[ch] = 1
            
   
    return freq == q

# --- How to use it ---
string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print("true")
else:
    print("false")
    
"""
Problem:
Check if two strings are anagrams of each other.

Algorithm:
1. Check if the lengths of the two strings are equal. If not, they cannot be anagrams.
2. Create a frequency dictionary for the first string, counting how many times each character appears.
3. Create a frequency dictionary for the second string in the same way.
4. Compare the two frequency dictionaries. If they are equal, the strings are anagrams;
    otherwise, they are not.

Time Complexity:
O(n), where n is the length of the strings (since we traverse both strings once).

Edge Cases:
- Strings of different lengths
- Strings with different characters 

Date Solved:
09 JULY 2026
"""