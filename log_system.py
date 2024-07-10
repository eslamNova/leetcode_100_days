# O(N)

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        r = 0 

        mback = "../"
        rem = "./"

        for log in logs:
            if log == mback:
                if r > 0:
                    r -= 1
            elif log == rem:
                pass
            else:
                r += 1
        return r
        