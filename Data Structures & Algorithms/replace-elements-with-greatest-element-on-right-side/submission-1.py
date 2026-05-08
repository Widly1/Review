class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Understand:
        # given an array arr,
        # replace every element in that array with the greatest element to its right
        # lastly, replace the last element with -1
        #  i.e ---> Input: arr = [2,4,5,3,1,2], Output: [5,5,3,2,2,-1]


        # Plan:
        # rather than using 2 pointers (my prev approach) we can simply start from the back of the array
        # we know that the very last number in the arr is going to be -1
        # so we can initialize it, lastNum = -1 
        lastMax = -1
        # then we want to reverse the loop by starting from the back to the front up until the 1st number
        for num in range(len(arr) -1 ,-1 ,-1):
            # then we want to find our new max number between our last max number and current number
            newMax = max(lastMax, arr[num])
            # now that we have our new max
            # we replace the current number we're on, with the last max from the list 
            # before the loop continues to move backwards
            arr[num] = lastMax
            # then we set our lastMax to be the newMax found after the switch is done
            # since it's the last big number found 
            lastMax = newMax
            # loop starts over and moves backwards until the 1st number is reached
        
        # then return the arr
        return arr