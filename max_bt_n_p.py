# Author: [islam ashraf]
# Date: [march 12 2025]
# Description: This script provides a solution to find the maximum count of positive or negative numbers in a list.
# Feedback: The solution is efficient and straightforward, effectively counting positive and negative numbers in a single pass.

# This class provides a solution to find the maximum count of positive or negative numbers in a list.
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Initialize counters for negative and positive numbers
        mn, mp = 0, 0
        
        # Iterate through each number in the list
        for n in nums:
            # Increment the negative counter if the number is negative
            if n < 0:
                mn += 1
            
            # Increment the positive counter if the number is positive
            if n > 0:
                mp += 1

        # Return the maximum count between positive and negative numbers
        return max(mp, mn)

# Complexity Analysis:
# Time Complexity: O(n), where n is the number of elements in the list 'nums'.
# This is because the solution iterates through the list once.
# Space Complexity: O(1), as the solution uses a constant amount of extra space regardless of the input size.
        