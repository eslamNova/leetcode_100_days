# O(LOGN)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) -1
        
        while left <= right:
            pivot = left + (right - left) // 2
            if target == nums[pivot]:
                return pivot
            if target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot -1
        return -1
                
        
        