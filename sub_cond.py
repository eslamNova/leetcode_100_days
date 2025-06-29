class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        ss = sorted(nums)
        l, r= 0, len(nums)-1
        ans = 0
        while l <= r:

            if ss[l] + ss[r] <= target:

                ans += 2 ** (r-l)

                l += 1
            else:
                r -= 1
        return ans % (10**9 + 7)

        