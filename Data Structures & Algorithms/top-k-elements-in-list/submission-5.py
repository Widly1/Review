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
        # num_map.items() returns a list of tuples where each tuple consists of a key-value pair
            # i.e.: (key, value)
        # key(telling our sorted function what to use as the criteria for sorting)
        # ^^ not the key from the dictionary btw, 
        # ^^ this key is specifically for the sorting 
        # = lambda (lambda is just an anonymous small function) 
        # x (is our parameter, the tuples (key, value) )
        # x[1] makes sure that the sorting is based on the second item of each tuple (key, -> the value <-)
        # reverse = true, just makes sure the sort is in descending order, greatest to least
        
        results = [item[0] for item in s_map[:k]]
         # this results line is saying:
         # for every item in the tuple s_map[but slicing the tuple to whatever value k is]:
            # so if k = 2, only look at the first 2 items from s_map
            # get item[0], which is the first value in the tuple (aka: the key)
            # ^^ i:e (key, value) == (item[0], item[1])
            # add the item[0] to the results list but stop at whatever the k value is
            # so if k = 2, only look at the first 2 items from the tuple 
            # this can be done because it's already sorted 
        print(s_map)
        print(results)
        return results 