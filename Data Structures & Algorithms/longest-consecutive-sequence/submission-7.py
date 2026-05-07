class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0     # to get the longest sequence
        streak_length = 0  # the length of the sequence and our incrementer

        for num in nums:
            if (num - 1) not in set_nums:
                streak_length = 1
                # we're using streaklength as an offset to get the next num
                # since streaklength = 1, (num + streak_length) == num + 1 
                # and so on as streak_length increases
                while (num + streak_length) in set_nums:  
                    streak_length += 1
                longest = max(streak_length, longest)
        return longest
            
            
