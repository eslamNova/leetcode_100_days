class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        i = 0 
        ans = 0

        for n in s:
            ans += abs(i - t.index(n))
            i += 1
        return ans
        