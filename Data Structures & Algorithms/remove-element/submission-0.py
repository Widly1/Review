class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Understand: we are given a list of nums & val is the number they want us to remove from that list
        # then they want us to return a list of numbers that exclude the val numbers that were removed
        # Plan: we will iterate through the current numbers list using the 2 pointers method
        # we will have a pointer locating val numbers and a pointer locating other numbers
        # then we will swap positions of those numbers, then increment the write pointer +1 
        # this will ensure we rewrite numbers only 1 time and we keep moving forward, if the replacement doesn't trip up the program
        # and if we find the numbers != val, then we can replace it with the other values   
        # r = read, w = write
        
        # w acts as the write pointer and also counts non-val elements
        w = 0

        # r acts as the read pointer to scan every element
        for r in range(len(nums)): 
            # If the current element is one we want to KEEP
            if nums[r] != val: 
                # Move it to the front at the next available write position
                nums[w] = nums[r] 
                # Move the write pointer forward
                w += 1 
        # w now represents the count of elements not equal to val
        return w 