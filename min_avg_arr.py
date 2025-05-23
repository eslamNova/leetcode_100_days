class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        sor = sorted(nums)
        l = len(nums)
        f = [] 
        for i in range((l//2)+1):
            # print(nums[i], nums[l-i-1])
            f.append((sor[i] + sor[l-i-1])/2)
            # print(f)
        return min(f)
        