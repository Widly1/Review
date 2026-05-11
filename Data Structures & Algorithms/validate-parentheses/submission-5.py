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
        # lastly we return the length of the stack
        return len(final) == 0