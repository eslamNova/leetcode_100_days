class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        ss = sorted(nums, reverse= True)[:k]
        ans = []
        c = Counter(ss)
        for n in nums:
            if c[n]>0:
                ans.append(n)
                c[n] -= 1
                if len(ans) == k:
                    break

        return ans
        