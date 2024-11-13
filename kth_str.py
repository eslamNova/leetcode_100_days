# O(N)
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        ans = []

        for n in arr:
            if c[n] == 1:
                ans.append(n)

        if len(ans) >= k:
            return ans[k-1]
        else:
            return ""