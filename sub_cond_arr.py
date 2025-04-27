"""
Problem: Count Subarrays with Special Condition
Given an array nums, count the number of subarrays of length 3 where the sum of first and last elements equals half of the middle element.

Time Complexity: O(n) where n is the length of nums
Space Complexity: O(1) as we only use a constant amount of extra space

Analysis:
- The current solution uses a simple sliding window approach with size 3
- For each window, we check if nums[i] + nums[i+2] == nums[i+1] / 2
- This is a straightforward implementation but could be optimized

Feedback (FAANG perspective):
1. Edge Cases: The solution doesn't handle empty arrays or arrays with length < 3
2. Type Hints: Good use of type hints, but could be more specific
3. Variable Names: 'ans' could be more descriptive
4. Documentation: Missing docstring and comments explaining the logic
5. Error Handling: No input validation

Optimization Opportunities:
1. We could use a more descriptive variable name for better readability
2. Add input validation for edge cases
3. Consider using a more efficient approach if the array is very large

Alternative Solution (in comments):
The current solution is actually quite efficient for this problem. However, if we needed to handle
floating-point precision issues, we could modify the comparison to use a small epsilon value.
"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Count the number of subarrays of length 3 where the sum of first and last elements
        equals half of the middle element.
        
        Args:
            nums (List[int]): Input array of integers
            
        Returns:
            int: Number of valid subarrays
            
        Raises:
            ValueError: If input array length is less than 3
        """
        # Input validation
        if len(nums) < 3:
            raise ValueError("Input array must have at least 3 elements")
            
        valid_subarrays = 0
        
        # Sliding window approach with size 3
        for i in range(len(nums) - 2):
            if nums[i] + nums[i+2] == nums[i+1] / 2:
                valid_subarrays += 1
                
        return valid_subarrays

# Alternative solution with floating-point precision handling:
"""
def countSubarrays(self, nums: List[int]) -> int:
    if len(nums) < 3:
        return 0
        
    EPSILON = 1e-10  # Small value to handle floating-point precision
    count = 0
    
    for i in range(len(nums) - 2):
        # Using abs() and epsilon for floating-point comparison
        if abs((nums[i] + nums[i+2]) - (nums[i+1] / 2)) < EPSILON:
            count += 1
            
    return count
"""
        