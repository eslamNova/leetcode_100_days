class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # p = 1
        # z = False
        # d = Counter(nums)
        # if d[0] > 1:
        #     return [0] * len(nums)
            
        # for n in nums:
        #     if n == 0:
        #         z = True
        #     else:
        #         p = p*n
        
        # ans = []
        # for n in nums:
        #     if z:
        #         if n != 0:
        #             ans.append(0)
        #         else:
        #             ans.append(p)
        #     else:
        #         ans.append(p//n)
        # return ans

        ans = [1] * len(nums)

        prefx = 1
        for i in range(len(nums)):
            ans[i] = prefx
            prefx *= nums[i]
        postfx = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfx
            postfx *= nums[i]
        return ans
        