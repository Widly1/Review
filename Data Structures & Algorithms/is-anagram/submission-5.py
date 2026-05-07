
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary that holds the the chars found in the first string
        # then iterate through the second str and see if the chars from there are in the dictionary
        s_dict= {}

        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        
        for char in t:
            if char not in s_dict:
                return False
            else:
                s_dict[char] -= 1
        # print(s_dict)
        
        for nums in s_dict.values():
            if nums != 0:
                return False
        return True
            