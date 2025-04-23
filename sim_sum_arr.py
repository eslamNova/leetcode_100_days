"""
LeetCode Problem: Count Largest Group

Problem Description:
Given an integer n, return the number of groups of size equal to the largest size.
A group is defined as numbers from 1 to n where the sum of digits of each number is equal.

Example:
Input: n = 13
Output: 4
Explanation: The groups are [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
The largest group size is 2, and there are 4 groups of size 2.

Time Complexity: O(n * log n) where n is the input number
Space Complexity: O(n) to store the groups
"""

from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Counts the number of groups that have the largest size.
        
        Args:
            n (int): The upper limit of numbers to consider (inclusive)
            
        Returns:
            int: The number of groups that have the largest size
        """
        # Dictionary to store groups where key is digit sum and value is list of numbers
        dc = defaultdict(list)

        # Iterate through all numbers from 1 to n
        for i in range(1, n+1):
            # Convert number to string to process each digit
            s = str(i)
            # Calculate sum of digits
            t = 0
            for j in s:
                t += int(j)
            
            # Add the number to its corresponding group based on digit sum
            dc[t].append(i)

        # Find the size of the largest group
        max_size = max(len(v) for v in dc.values())
        
        # Count how many groups have the maximum size
        ans = 0
        for d in dc.values():
            if len(d) == max_size:
                ans += 1
        return ans
        