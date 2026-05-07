class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        l = 0
        r = len(lowercase) - 1

        while l < r:
            if not lowercase[l].isalnum():
                l +=1 
                continue
            if not lowercase[r].isalnum():
                r -=1
                continue 
            if lowercase[l] != lowercase[r]:
                return False
            l += 1
            r -= 1
        return True

        