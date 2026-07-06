s = "banana"
freq = {}

# s_set becomes {'b', 'a', 'n'}
s_set = set(s) 

for char in s_set:
    freq[char] = s.count(char)

print(freq)

"""
Problem:
Find the first non-repeating character in a string.

Algorithm:
1. Create a set of unique characters from the string.
2. Count the frequency of each character in the string. 

Time Complexity:
O(n)

Edge Cases:
- Empty string
- String with all repeating characters

Date Solved:
06 JULY 2026
"""