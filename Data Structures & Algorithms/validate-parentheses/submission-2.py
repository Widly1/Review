"""
    this is the KEY:
    i.e: s = "([{}])"
    Output: true
    * It is noticeable that in this case, regardless of the number of chars exists
        each one is closed at it's corresponding location meaning, 
        * the 1st '(' is the last ')' 
        * the 2nd '[' is the 2nd to last ']' 
        * the 3rd '{' is the 3rd to last '}'
        So key takeaway is that the positions must match in reverse order 
    * we need a reference list for matching closing to open 
    * and we need a stack to append and pop from 
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # our dict for referencing and matching open to close chars
        ref = {"}" : "{" , ")" : "(" , "]" : "["}
        stack = []
        
        # for the chars in string s
        for c in s:
        # if the current char is in the reference:
            if c in ref:
                # check if the current char referenced matches the last item in the stack and make sure the stack isn't empty
                if stack and ref[c] == stack[-1]:
                    # pop the item from the stack
                    stack.pop()
                # else if it doesn't match, automatically return false since the pattern is invalid
                else:
                    return False

            # else if the current item isn't in the reference, add that item to the stack
            else:
                stack.append(c)
        
        # then outside of this for loop we want to check if the stack is empty or not then return True or
        if stack: 
            return False
        return True

        