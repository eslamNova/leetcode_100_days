# O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for l in s:
            if l.isalnum():
                r += l.lower()
        
        return r == r[::-1]
        
        