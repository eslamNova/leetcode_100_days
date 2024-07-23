# O(N.LogN)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        ans = []
        ans = sorted(nums, key=lambda x: (c[x], -x))
                

        return ans