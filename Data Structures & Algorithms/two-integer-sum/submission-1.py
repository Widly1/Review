class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        create a empty dict
        we can create a difference variable diff = target - current num
        iterate through the list to add the values and their index in the dict 
        if the target - current num is in our dictionary (the difference)
        then we return the current num[index] and the difference[index] which should be in our dictionary
        """
        s_dict= {}
        for index, num in enumerate(nums):
            difference = target - num
            
            if difference in s_dict:
                return [s_dict[difference], index]

            s_dict[num] = index

        


               