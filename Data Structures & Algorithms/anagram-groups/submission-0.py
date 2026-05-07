"""
U
- An anagram is a string that contains the exact same characters as another string, 
- but the order of the characters can be different.
- group all anagrams together into sublists.
i.e.:
    - Input: strs = ["act","pots","tops","cat","stop","hat"]
    - Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

P
- we can iterate through the list of words
- we know that a str is an anagram if they contain the same letters, regardless of the order
- so we can create a default listed dictionary with default dict
- we can create a hashmap to store the sorted words or str as keys 
- and their values can be the strs from the original list that match the characters from the key
- then we can simply return the values from that list
    - this will give us the correct answer because in the hashmap the sorted words are keys,
    - if any char from the strs list match the keys in the map
    - they will automatically be associated with that specific key
    - so returning the values from the hashmap will already have grouped all matching anagrams

"""
from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create our list type dictionary
        dict1 = defaultdict(list)

        for char in strs:
        # sort the chars in strs to use them as keys for our dictionary
            sorted_char = tuple(sorted(char))
        # then based on the sorted key, append the chars that match with it
            dict1[sorted_char].append(char)
        
        return list(dict1.values())


        