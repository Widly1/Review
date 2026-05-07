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
"""
class Solution:
    def isValid(self, s: str) -> bool:
        ref = {"}" : "{" , ")" : "(" , "]" : "["}
        stack = []

        for i in s:
            if i in ref:
                # if the current char is in the ref list
                # we have to make sure the stack isn't empty 
                # and that the last item stack[-1] matches the current referenced char ref[i]
                if stack and stack[-1] == ref[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        return False





        
       