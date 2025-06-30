class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        m = 0 
        for n in c:
            s = 0
            if n+1 in c:
                s = c[n] + c[n+1]
                if s > m:
                    m = s 
        return m