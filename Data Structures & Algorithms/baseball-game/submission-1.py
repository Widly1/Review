class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Plan:
        # We have to initialize our empty stack that is going to hold the total score found
        # initialize what our variable +, D, and C are supposed to do in the stack
        # + = push the sum of the previous two scores. ==> our stack has to understand this operation if it finds a +
        # D = push a new score that is the double of the previous score. ==>  *2 our previous val if we find a D
        # C = pop whatever was the last input into the stack or subtract it from the total score
        # In order to do this we'd have to iterate through our operations array
        # as we go through the array, we push and pop to our score stack
        # we do calculations based on the string found in the operations array into our stack
        # then we sum the values added to our stack as the final result 

        score = []

        for char in operations:
            if char == '+': # add our previous 2 numbs from the stack
                score.append(score[-1] + score[-2])
            elif char == 'D':
                score.append(score[-1] * 2) # the double of the previous score
            elif char == 'C':
                score.pop() # pop whatever was the last input into the stack
            else:
                score.append(int(char)) # if its a number
                                        # simply push to the stack from operations
        return sum(score) #return the sum of all values into the stack
