class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)<1:
            return []
        if len(nums)<2:
            return [str(nums[0])]
        l,r = 0,1
        ln, rn = 0,0
        s = ""
        c = 1
        f = True
        ans = []
        while r < len(nums):

            if nums[r] - nums[l] == c:
                if f:
                    s += str(nums[l]) + "->"
                    f = False
                c += 1
                r += 1

            else:
                s += str(nums[r-1])
                ans.append(s)
                s = ""
                f = True
                c = 1
                l = r
                r += 1
            
            # print(s)
        if s:
            ans.append(s+str(nums[r-1]))
        else:
            ans.append(str(nums[r-1]))
        return ans

