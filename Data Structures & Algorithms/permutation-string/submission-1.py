"""
based on test case 1 and 2, we can highlight that in order for it to be true:
the window has to contain each of the char without any chars interrupting the sequence
it also has to be the same length of the s1 string, meaning it can't be "lecaabee" 
"lecaabee" is false because the 2nd a in the window of [c,a,a,b] makes the length of the window longer than s1

so to solve this we have to:
iterate through our s2
create our window
add to our window when we find the first char that matches in s1
    else if that char doesn't match, we want to shrink our window by removing the char that was added in our window by removing from the left
as our window grow based on what we find 
if we come across a char that's in s1 and already in our window we add it to our window, 
    - then compare in order to determine whether or not we are going to drop from the left and whether or not this will make our window valid
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # create our counter variables for both the window and s1
        s1_count = Counter(s1)
        window_count = Counter()
        l = 0

        for r in range(len(s2)):
            # increase our window count for each char we see in s2
            window_count[s2[r]] += 1
            
            #create our window (calculate our actual window size)
            window = (r - l + 1)

            # if our window is greater than s1, remove from it, Leftmost out
            if window > len(s1):
                window_count[s2[l]] -= 1
            # check the frequency of that specific char in order to fully remove it
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                # move L forward afterwards
                l += 1
            
            # check frequency between the 2 maps
            if window_count == s1_count:
                return True
        return False
        

