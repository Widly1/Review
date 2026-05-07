class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        l = 0
        r = len(lowercase) - 1
        symbols = set(r"""~!@#$%^&*()_-+={[}}|\:;"'<,>.?/ """)

        while l < r:
            if lowercase[l] in symbols:
                l += 1 
                continue
            if lowercase[r] in symbols:
                r -= 1 
                continue
            elif lowercase[l] != lowercase[r]:
                return False
            l += 1
            r -= 1
        return True
