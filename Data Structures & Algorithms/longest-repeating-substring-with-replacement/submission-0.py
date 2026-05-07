from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        we can use a dictionary to keep track of the chars seen and their frequency
        then we can determine which char we want to increase the value for based on whichever one is seen the most
        we can iterate through the string and increase the frequency of each char that we see
        then we do a comparison between the chars and their value
        then whichever char has the most frequency, we simply update it's count with the k value given
        i.e: 
            Input: s = "XYYX", k = 2
            Output: 4

            Input: s = "AAABABB", k = 1
            Output: 5
        """

     
        l = 0
        r = 0
        maxFreq = float('-inf')
        counter = defaultdict(int)
        res = 0

        while r < len(s):
            counter[s[r]] += 1
            maxFreq = max(maxFreq, counter[s[r]])

            window = r - l + 1

            while window - maxFreq > k:
                counter[s[l]] -= 1
                l += 1
                window = r - l + 1
            
            res = max(res, window)
            r += 1

        return res
  


        