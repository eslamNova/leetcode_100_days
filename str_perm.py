# O(N)

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        k = []
        for i in range(n):
            k.append(i)
        i,d = 0,n
        ans = []
        for j in s:
            if j == "I":
                ans.append(i)
                i += 1
            else:
                ans.append(n)
                n -= 1
        ans.append(i)
        return ans