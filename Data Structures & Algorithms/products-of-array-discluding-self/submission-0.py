class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        l = len(nums)
        n_l = l * [1]

        for i in range(len(nums)):
            n_l[i] = pre
            pre *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            n_l[i] *= post
            post *= nums[i]
        
        return n_l
