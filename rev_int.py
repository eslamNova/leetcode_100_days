class Solution:
    def reverse(self, x: int) -> int:

        mx, mn = 2**31 -1, -2**31
        # print(x,mx)
        if x == 0 or x > mx or x < mn:
            return 0
        
        m = x > 0
        s = str(x)

        
        if not m:
            s = s[1:]
            o = int(s[::-1])
            o *= -1
        else:
            o = int(s[::-1])

        if o > mx or o  < mn:
            return 0
        return o
        