"""
U
- we have a list of nums and need to find the target using nums from the list
- return the index of said nums that when combined, adds up to the target

P
- we can initialize an empty dict to hold the values from the list
- then we can create a variable called differnce, which will be the values in the dict - target
- that way if the target - num (num from the list we're on) is in the dict (difference)
- then return the index of the num(from the list), and the index of the difference(from the dict)

I
- create empty dict
- create difference variable
- iterate through list of nums, both the numbers and the indeces
    - create logic to check if the difference (target - num) is in the dict or not
        - return [the dictionary[index] where difference is, num[current_num_index]]
    - else, add that current_num to the dictionary, and it's value (it's index from the nums list)
"""
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

            
               