class Solution:
    def isValid(self, s: str) -> bool:
        # we create our ref dictionary
        ref = {"}":"{", ")":"(", "]":"["}

        # create our empty stack
        final = []

        # initialize our pointer
        f = 0

        # now we iterate through our string
        while f < len(s):
            # check to see if our current string is a closing bracket in our ref dictionary
            if s[f] in ref:
                #check the length of our stack for edge case
                if len(final) == 0:
                    return False
                # if it is then we need to check if it's the matching bracket to the last item in our stack
                if ref[s[f]] == final[-1]:
                    # if this is true then remove it from our stack
                    final.pop()
                    # then continue to the next
                    f +=1
                else: # If the bracket doesn't match the top of the stack
                    # we just return false
                    return False
            
            else: # if the current string isnt a closing bracket 
                final.append(s[f])
                # then continue to the next
                f +=1 
        # lastly we return the length of the stack (True or False)
        return len(final) == 0

        #----- solution 2 (for loop)
        # ref = {")": "(", "}": "{", "]": "["}
        # stack = []

        # for char in s:
        #     # check to see if the character is a closing bracket
        #     if char in ref:
        #         # check if the stack is empty BEFORE we try to look at it
        #         if len(stack) == 0:
        #             # If we see a closing bracket but the stack is empty, 
        #             # there was never an opening bracket for it.
        #             return False
                
        #         # take the last item off the stack
        #         top_item = stack.pop()
                
        #         # does the opening bracket we just popped match the partner of our current closing bracket?
        #         if ref[char] != top_item:
        #             # if they don't match (e.g., we have '(' but found ']')
        #             return False
            
        #     # if it wasn't a closing bracket, it must be an opening one
        #     else:
        #         stack.append(char)

        # return len(stack) == 0