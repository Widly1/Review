"""
initialize a empty dict to hold the numbers from the array nums
    - set each number as a key, and 
    - their value can be a count of how many times they appear
then we want to check whether or not:
- any key in the array has a value greater than 1
- meaning they've appeared more than 1x; they have a duplicate
- return true or false based on outcome
"""
class Solution:
 
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # solution 1 using hashmap (01/03/2025, 7pm)
        # num_dict  =  {}

        # for key, num in enumerate(nums):
        #     if num not in num_dict:
        #         num_dict[num]= 1
        #     else:
        #         num_dict[num] += 1
        # # print(num_dict)

        # for num in num_dict.values():
        #     if num > 1:
        #         return True
        # return False

    ## solution 2 using hashset, 1 for loop, better efficiency (01/03/2025, 8pm)

        # # initialize empty set
        # num_dict = set()

        # # for num in nums array
        # for num in nums:
        #     # if number is in hashset already
        #     if num in num_dict:
        #     # return True, meaning there's a duplicate 
        #     # and there's no need to continue with the rest of the numbers
        #         return True
        #     # else add the num to the hashet(num_dict) and continue to the next
        #     else: 
        #         num_dict.add(num)
        #  # since sets don't allow duplicates
        #  # return false since we've gone through the entire list and added all numbers 1x to the list
        #  # meaning there are no dups
        # return False
    
     ## solution 3 using hashset and original list, more concise (01/03/2025, 8:30pm)
      
      # so for this approach I used the set method to remove any dups from the orinal list
      # kept the original list as list1 = nums
      # then simply compared the lengths; since the num_dict is just the original list without dups
      # if there are no dups then the return after comparing the length of both lists, (if the same length) should be false
      # else if one length is different than the other return True, meaning there are dups somewhere in nums

        # set with the values from nums
        num_dict = set(nums)
        list1 = nums

        #
        if len(num_dict) != len(list1):
            return True    
        return False

            # 3 LINES OF CODE, NO FOR LOOPS AND A SINGLE LOGIC STATEMENT  
            




         