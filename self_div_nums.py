class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right+1):

            s = str(i)
            if "0" in s:
                continue
            bad = False
            for n in s:
                if i % int(n) != 0:
                    bad = True
            if not bad:
                ans.append(i)
        return ans
                    
        