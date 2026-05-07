class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Result list to store unique triplets
        res = []
        
        # Step 1: Sort the array to apply two-pointer technique
        nums.sort()

        # Step 2: Iterate through the list with `index` as the first element of the triplet
        for index, value in enumerate(nums):
            # If the first number is greater than 0, stop searching (since sorted array means all numbers after it are > 0)
            if value > 0:
                break

            # Skip duplicate elements to avoid duplicate triplets
            if index > 0 and value == nums[index - 1]:
                continue

            # Step 3: Use two-pointer technique to find pairs that sum to -value
            l, r = index + 1, len(nums) - 1  # Left and right pointers

            while l < r:
                total = value + nums[l] + nums[r]  # Sum of three numbers
                
                # If sum is too large, move the right pointer left
                if total > 0:
                    r -= 1
                # If sum is too small, move the left pointer right
                elif total < 0:
                    l += 1
                # Found a valid triplet
                else:
                    res.append([value, nums[l], nums[r]])  # Add the triplet to results
                    
                    # Move both pointers to find the next unique triplet
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for `l` to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        # Return all unique triplets found
        return res
