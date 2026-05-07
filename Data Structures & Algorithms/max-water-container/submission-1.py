class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0

        while left < right:
        # after initializing left and right, find the min between the two
        # this will serve as the water lvl(since water can't go higher than the shorter wall).
            water_lvl = min(heights[left], heights[right])

            # then find the width (which is the number of spaces between the 2 heights) 
            width = right - left

            # then calculate the area which is water lvl * width
            area = water_lvl * width

            # then we choose the max between the area and largest
            largest =max(largest, area)

            # move pointers based on whichever one is smallest
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1 
        
        return largest


        