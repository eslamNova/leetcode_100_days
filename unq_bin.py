class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        res = ""
        for i in range(n):
            if nums[i][i] == "1":
                res += "0"
            else:
                res += "1"
        return res