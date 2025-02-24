import sys
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        s = ""
        for n in num:
            s += str(n)

        r = k + int(s)

        ans = [] 
        for n in str(r):
            ans.append(int(n))

        return ans 