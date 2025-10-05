class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        q = 0
        for i in range(len(nums)-1):
            a = int(str(nums[i])[0])
            for j in range(i+1, len(nums)):
                b = int(str(nums[j])[-1]) 
                if math.gcd(a, b) == 1:
                    q += 1
        return q
        