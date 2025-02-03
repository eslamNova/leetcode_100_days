class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1,1
        ans = [1]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc += 1
                ans.append(inc)
                dec = 1
            elif nums[i] > nums[i+1]:
                dec += 1
                ans.append(dec)
                inc = 1
            else:
                inc, dec = 1,1
                
        return max(ans)
                