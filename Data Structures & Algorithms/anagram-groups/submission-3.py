from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = defaultdict(list)

        for char in strs:
            
            sorted_keys = tuple(sorted(char)) # sort the characters from the string
            
            dict1[sorted_keys].append(char)  # if the sorted key match a char in the string
                                            # add that char as a value to the key

        return list(dict1.values()) # return the values of each key grouped as a list
        
        