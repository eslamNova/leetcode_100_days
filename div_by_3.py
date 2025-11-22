class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        o = 0 

        for n in nums:
            p = n % 3
            if p != 0:
                if p <= 1:
                    o += p
                else:
                    o += 1
            
        return o 
            