class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        count = 0

      
        for r in range(len(s)): 
            # if the current char is already in the set
            # remove if it is
            while s[r] in sets: 
                sets.remove(s[l])   
                l += 1  # then we move the left pointer up 1     

            sets.add(s[r])

            window = r - l + 1 # create our window
            
            #update the max window we've found
            count = max(count, window) 

        return count

            
