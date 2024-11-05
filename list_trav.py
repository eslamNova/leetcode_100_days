# O(N)

from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        # Initialize leftMin and rightMin arrays
        leftMin = [float('inf')] * n
        rightMin = [float('inf')] * n
        
        # Fill leftMin array
        leftMin[0] = nums[0]
        for i in range(1, n):
            leftMin[i] = min(leftMin[i-1], nums[i])

        # Fill rightMin array
        rightMin[-1] = nums[-1]
        for j in range(n-2, -1, -1):
            rightMin[j] = min(rightMin[j+1], nums[j])

        min_sum = float('inf')
        found = False

        # Traverse from i = 1 to n-2 and check for mountain triplets
        for j in range(1, n-1):
            if nums[j] > leftMin[j-1] and nums[j] > rightMin[j+1]:
                found = True
                current_sum = leftMin[j-1] + nums[j] + rightMin[j+1]
                min_sum = min(min_sum, current_sum)
        
        return min_sum if found else -1
