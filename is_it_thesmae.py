# O(NlogN)
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l = [s1,s2,s3]
        t = len(s1) + len(s2) + len(s3)
        m = sorted(l, key=len)[0]
        
        for i in range(len(m), 0, -1):
            k = m[0:i]
            if s1.startswith(k) and s2.startswith(k) and s3.startswith(k):
                return t - (i * 3)

        return -1        