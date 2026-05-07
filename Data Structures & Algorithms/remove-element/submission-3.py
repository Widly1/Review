class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Understand:
        # given an integer ARRAY NUMS & integer VAL 
        # remove all occurrences of VAL in place
        # after we remove all VALs from the list, return the COUNT of numbers left
        # To be accepted, the first elements of nums must contain only elements NOT EQUAL to VAL

        # Plan: 
        # Since we have to keep track of the numbers being kept, we NEED a COUNTER
        # This counter will also point to where we are in the list
        c = 0
        # we have to iterate through the nums list, and determine what should be removed
        for k in range(len(nums)):
        # once we find what needs to be removed; by ignoring nums that are valid
            if nums[k] != val:
        # we should swap its place with something that should be kept
                nums[c], nums[k] = nums[k], nums[c]
        # as we swap places, we increase the count (and our location) as well since its a valid number
                c += 1
        # then we return the amount of times we've swapped or the COUNT of valid nums found
        return c

        
       