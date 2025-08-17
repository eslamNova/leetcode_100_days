class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        s = sorted(nums)
        # print(s)
        mabs = 0 
        for i in range(len(s)):
            if s[i] < 0:
                s[i] = -1 * s[i]
                k -= 1
            elif s[i] > 0:
                if k % 2 == 0:
                    k = 0
                else:
                    mabs = min(s)
                    k = 0 
            else:
                k = 0
            
            # print(s)
            if k == 0:
                break
        if k % 2 > 0:
            mabs = min(s)
                
        return sum(s) - (2* mabs)
        