class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        o,e = [], []
        
        for i in range(len(nums)):
            if i % 2 ==0:
                e.append(nums[i])
            else:
                o.append(nums[i])

        o = sorted(o)[::-1]
        e = sorted(e)

        ans = []
        
        for i in range(len(nums)):
            if i %2 == 0:
                ans.append(e.pop(0))
                
            else:
                ans.append(o.pop(0))
                
        return ans