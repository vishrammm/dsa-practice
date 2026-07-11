from collections import defaultdict

def groupAnagrams(strs):
    # Create a map where the value defaults to an empty list
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Sort the word to create the unique key
        # 'eat' -> ['a', 'e', 't'] -> 'aet'
        sorted_key = "".join(sorted(word))
        
        # Append the original word to the list matching that key
        anagram_map[sorted_key].append(word)
        
    # Return just the grouped lists
    return list(anagram_map.values())

# Example execution:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]