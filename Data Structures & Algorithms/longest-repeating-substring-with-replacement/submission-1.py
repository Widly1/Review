class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window method
        """
        l = 0
        maxC = 0
        counter = defaultdict(int)
        res = 0

        for r in range(len(s)):
            # for each char we see, we add it to the dict
            counter[s[r]] += 1
            
            # get our current max
            maxC = max(maxC, counter[s[r]])

            #create our window
            window = r - l + 1

            # if our current window - the current char count is greater than k
            while window - maxC > k:
                # we want to remove from the left of the window
                counter[s[l]] -= 1
                l += 1
                # update our window
                window = r - l + 1
            
            res = max(res, window)
        return res 
                
        
  


        