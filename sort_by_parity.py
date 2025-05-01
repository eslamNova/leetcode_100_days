class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = [] 

        for n in nums:
            if n % 2 == 0:
                ans.insert(0,n)
            else:
                ans.append(n)
        return ans