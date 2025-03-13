from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """
        Determines if it's possible to reduce an array to all zeros using given queries.
        
        Args:
            nums (List[int]): The input array of non-negative integers
            queries (List[List[int]]): List of queries where each query is [start, end] representing
                                      an operation that decrements all elements from index start to end by 1
        
        Returns:
            bool: True if it's possible to reduce all elements to 0, False otherwise
        
        Time Complexity: O(n + q) where n is length of nums and q is number of queries
        Space Complexity: O(n) for the difference array
        
        Algorithm:
        1. Uses difference array technique to efficiently track cumulative operations
        2. For each query, marks +1 at start and -1 at end+1 in difference array
        3. Computes prefix sum to get total operations at each index
        4. Checks if operations are sufficient to reduce each number to zero
        """
        # Length of input array
        N = len(nums)
        # Initialize difference array with one extra space for boundary handling
        df = [0] * (N+1)

        # Process each query using difference array technique
        for q in queries:
            df[q[0]] += 1          # Add 1 at start of range
            df[1+q[1]] -= 1        # Subtract 1 after end of range

        # Calculate prefix sum to get total operations at each index
        for i in range(1, N+1):
            df[i] += df[i-1]
        
        # Check if number of operations is sufficient for each element
        for i in range(N):
            if df[i] < nums[i]:    # If operations are less than required
                return False
        return True
        