"""
U
- An anagram is a string that contains the exact same characters as another string
- but the order of the characters can be different.

P
- we can use a hashmap to assign each character from one of the strings as a key, 
    -and their value as the amount of time they appear
- then we can create a final logic statement to return True or false if both dictionaries match

I
- 2 empty dicts, for s and t
- add characters to from s and t to their corresponding dictionaries
- then compare if both dictionaries match in the end, to get true or false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict1 = {}
        dict2 = {}

        for char in s:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1 
        
        for char in t:
            if char not in dict2:
                dict2[char] = 1
            else:
                dict2[char] += 1 
        print(dict1)
        print(dict2)

        return dict1==dict2

       