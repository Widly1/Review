from collections import deque
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxs = []
        tracker = deque()

        for r in range(len(nums)):

            #while our dq isn't empty 
            #and the last number in the dq is less than the current number we're on, 
            # we want to remove that number from the dq
            while tracker and nums[tracker[-1]] < nums[r]:
                tracker.pop()

            # we want to add our current number to the dq
            tracker.append(r)

            #then check if the leftmost num in our dq is outside our window
            # in order to remove
            # logically L is were our window begins, 
            # so anything less than L index wise, is outside of our window/invalid
            if tracker[0] < l:
                tracker.popleft()

            # we want to create our window size
            window= r - l + 1

            # if we've reached the k length of our window, we have to slide our window
            if window == k:
                # add the value at that current index to our list of results
                maxs.append(nums[tracker[0]])
                l += 1 # then move our window

        return maxs