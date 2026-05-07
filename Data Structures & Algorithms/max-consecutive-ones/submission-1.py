class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Understand: we want to return the max number of 1's that are in the array together
        # Implement:
        # we should have a maxValue variable 
        # that will compare the current count we're at before we lost the pattern of 1's vs the previous max (or current max)
        # we can iterate through the array, 
        # for every 1 we find we increase the count of 1's found, then we check if the current count is the max between overall max value
        # then we return the max

        maxOnes = 0
        currentOnes = 0

        for numbers in nums: #for every number in the list nums
            if numbers == 1: # if the number we're at is equal to 1
                currentOnes += 1  # increase our currentOnes count +1
                maxOnes = max(maxOnes, currentOnes) # then perform a comparison between currentOnes and maxOnes to get the max 
            else:
                currentOnes = 0 # else return the count to 0 to start over 
        return maxOnes #then return the maxOnes found 