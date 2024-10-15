# O(N)
class Solution:
    def minimumSteps(self, s: str) -> int:
        lst = [int(i) for i in s]
        trn = 0
        zer = 0
        summ = 0
        for i in lst:
            if i:
                if zer > 0:
                    summ += trn * zer
                    
                trn += 1
                zer = 0
            else:
                zer += 1

        if zer > 0:
            summ += zer * trn

                


        return summ

