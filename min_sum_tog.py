# O(NLogN)

class Solution:
    def splitNum(self, num: int) -> int:

        n = sorted(list(int(x) for x in str(num)))
        n1, n2 = "", ""
        tog = True
        for i in n:
            if tog:
                n1 += str(i)
                tog = False
            else:
                n2 += str(i)
                tog= True
        

        return int(n1) + int(n2)

        