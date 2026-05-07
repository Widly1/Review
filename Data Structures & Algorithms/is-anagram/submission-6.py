class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #immediate edge case if s and t aren't the same length
        if len(s) != len(t):
            return False
        # add s letters to the dictionary w a value of 1 and increment as needed
        # loop through t and if the letter in T is found in s, remove the count -1
        # if the char found in t not in s, return false 
        # else we just decrement as we move along until the dict has a value of 0

        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char not in s_dict or s_dict[char]==0:
                return False
            s_dict[char] -=1
        return True