class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_map = {}
        results = []

        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1
        
        s_map = sorted(num_map.items(), key=lambda x: x[1], reverse=True)
        results = [item[0] for item in s_map[:k]]
        
        return results
        