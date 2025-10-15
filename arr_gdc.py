class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        return math.gcd(mx,mn)

        