class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # understand:
        # Create an array ans of length 2n, meaning create a new empty array 
        # where ans[i] == nums[i] , meaning each value of the new array matches the values of the old array
        # ans[i + n] == nums[i], For each position i in the original array nums
        # Place that value at position i + n in the answer array

        # Plan:
        # initialize our new empty array
        ans = [] 
        # go through our old array and add the values to the new array
        for i in range(len(nums)):
            ans.append(nums[i])
        # repeat this process 2x since the size of our new array is twice the original
        return ans * 2