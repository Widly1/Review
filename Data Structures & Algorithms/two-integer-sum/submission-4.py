class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        #iterate thru nums list
        for position, num in enumerate(nums):
            # create difference
            difference = target - num
            # if the difference is in dict already:
            # meaning target -  current_num_from_numslist 
            if difference in dict1:
            # return the index of the difference value
            # return the index from the current_num_from_numslist
                return [dict1[difference], position]
            # else add current_num_from_numslist with the value being the index(position)
            # i.e. : nums = [3,4,5,6]
            #        dict1 = {3 : 0, 4: 1 , 5: 2, 6: 3}
            dict1[num] = position

     
