class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Understand:
        # given an array arr,
        # replace every element in that array with the greatest element to its right
        # lastly, replace the last element with -1
        #  i.e ---> Input: arr = [2,4,5,3,1,2], Output: [5,5,3,2,2,-1]

        # Plan:
        # rather than using 2 pointers (my prev approach) we can simply start from the back of the array
        # we're going backwards because we have to find the biggest number to the RIGHT of the current number
        # we know that the very last number in the arr is going to be -1
        # so we can automatically initialize it as our lastMax before doing the in-loop comparison 
            # ----since there's nothing to compare to the right of the last number, its gonna be -1
        # then as we go through the array starting from the back
        # we have to find the our new max, which would be our currentnumber vs the previous max (lastmax)
        # once that's found we have to update our current number w last max 
            #--since it's the last greater number to the right of our current number
        # then we update our last max for our new max for the next comparison when the loop runs again 

        # automatically initialize lastMax as -1 before doing the comparison in the loop
        lastMax = -1
        # we're going backwards
        for num in range(len(arr) -1, -1, -1):
            # find the our new max
            newMax = max(arr[num], lastMax)
            # swap our current number w the last max we saw
            arr[num] = lastMax
            # then we swap our last max for our new max for the next comparison
            lastMax = newMax
        return arr


        