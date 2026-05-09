class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # understand:
        # Create an array ans of length 2n, meaning create a new empty array 
        # where ans[i] == nums[i] , meaning each value of the new array matches the values of the old array
        # ans[i + n] == nums[i], For each position i in the original array nums
        # Place that value at position i + n in the answer array

        # Plan:
        # initialize our new empty array
        # ans = [] 
        # go through our old array and add the values to the new array
        # for val in nums:
        #     ans.append(val)
        # repeat this process 2x (or x2 the new arr) since the size of our new array is twice the original
        # return ans * 2

        #  or to showcase concatenation under the hood use a nested for loop
        ans= []
        for i in range(2):
            for val in nums:
                ans.append(val)
        return ans