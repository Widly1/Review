class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        dict1 = {}


        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            dict1[i] += 1
        
        sorted_dict1 = list(dict1.items()) # -> turn the dict into a list of tuples
        sorted_dict1.sort(key=lambda x: x[1], reverse = True) 
        #=> we sort the values from the dict using the key as the argument 
        #=> for each x element in the list use the 2nd item (x:x[1])
        #=> then we reverse the order for highest to lowest value
        
        for i in range(k):
            # Only append the element(at index 0), not the count
            result.append(sorted_dict1[i][0]) 
            
        return result
    # return result