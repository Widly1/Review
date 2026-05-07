class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        """
        1-index means the indeces start 1 to n, 
        rather than 0 to n like usual in an array
        """

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:  # we've found the exact numbers and their +1-index
                return [l + 1, r + 1]
        return []
