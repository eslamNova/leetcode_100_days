class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        ans = []
        add = 0
        first = True
        for i in range(len(nums)-1):
            
            if nums[i] < nums[i+1]:
                if first:
                    add += nums[i]
                    first = False
                add += nums[i+1]
            else:
                ans.append(add)
                add = 0 
                first = True
        ans.append(add)
        
        if max(ans) < max(nums):
            return max(nums)
        return max(ans)
            

        