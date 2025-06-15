class Solution:
    def minElement(self, nums: List[int]) -> int:

        ans = []

        for n in nums:

            s = str(n)
            x = 0
            for j in s:
                x += int(j)
            ans.append(x)
            
        return min(ans)
        