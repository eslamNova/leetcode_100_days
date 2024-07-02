# O(N+M)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        for n in nums1:
            if n not in ans:
                if n in nums2:
                    m = min(c1[n], c2[n])
                    for i in range(m):
                        ans.append(n)

        return ans