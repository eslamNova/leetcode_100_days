class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cs = ""
        rs = ""
        for n in s:
            if n != "-":
                cs += n.upper()

        l = len(cs)
        i = 0
        if l % k != 0:
            i = l%k
            rs += cs[:i]
            rs += "-"
            cs = cs[i:]
        # print(rs)
        g = l // k

        for j in range(0,l, k):
            rs += cs[j:j+k]
            rs += "-"
            # print(rs)
        r = 0
        for n in range(len(rs)-1, -1,-1):
            if rs[n] == "-":
                r +=1
            else:
                break
        

        return rs[:len(rs)-r]
            


            

        