class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = sorted(nums1 + nums2)
        n = len(new)
        if n % 2 == 0:
            return (new[n//2] + new[n//2-1]) / 2
        return new[n//2]