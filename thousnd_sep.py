class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        a = ""

        if len(s) < 4:
            return s
        c  = 0 
        for i in range(len(s)-1, -1 , -1):
            c += 1
            a += s[i]
            if c == 3 and i > 0:
                a+= "."
                c = 0
        return a[::-1]
        