from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = defaultdict(list)

        for char in strs:
            
            sorted_key = tuple(sorted(char))
            
            dict1[sorted_key].append(char)

        return list(dict1.values()) # return the values of each key grouped as a list
        
        