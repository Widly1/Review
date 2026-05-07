class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:

        n_set = set(nums)

        return len(n_set) != len(nums)
       