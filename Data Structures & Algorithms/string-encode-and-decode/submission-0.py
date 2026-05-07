class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for c in strs:
            ans += str(len(c)) + "#" + c

        # print(ans)
        return ans

        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i   # initialize our j pointer in the same spot as i

            while s[j] != "#": # while j isn't at our delimeter 
                j += 1      # we increment j to the next char
            
            length = int(s[i:j]) # our length becomes the int value from where i started to the spot before j
            
            stop_point = j + 1 + length  # the stopping index, the index just after the final char
            # j + 1 = start from the spot after the '#'
            #  + length = the number of chars the word has. i.e: 1 + 5 chars = 6 
        
            res.append(s[j + 1: stop_point])  # so we slice from the first char, to the stopping index(before the start of our next word)

            i = stop_point # we move i to the last_char(the stopping index) from the previous word
            # then the loop starts again at j = last_char, which is at our delimeter
            # then j+= 1, moves us to the 1st char in the next word

        return res



            
