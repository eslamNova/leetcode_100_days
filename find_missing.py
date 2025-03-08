from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Find the repeated and missing values in a square grid.
        
        Args:
            grid (List[List[int]]): An n x n grid containing integers from 1 to n^2,
                                   where one number is repeated and one is missing.
        
        Returns:
            List[int]: A list containing [repeated_value, missing_value]
        
        Example:
            Input: grid = [[1,3],[2,2]]
            Output: [2,4]  # 2 is repeated, 4 is missing
        
        Complexity Analysis:
            Time: O(n²) where n is the side length of the grid
                - O(n²) for grid flattening and sum operations
                - O(n²) for set conversion
                - O(n²) for the final loop
            Space: O(n²)
                - O(n²) for storing the set of numbers
                - O(1) for the output list
        
        Engineering Notes:
            Pros:
            - Simple and readable implementation
            - Memory efficient for small to medium sized grids
            - Good use of Python's built-in functions
            
            Cons:
            - Not optimal for very large grids due to O(n²) time complexity
            - Multiple iterations over the data
            - The zip(*grid) operation could be memory intensive for large grids
            
            Potential Improvements:
            1. Could be optimized to O(n²) with single pass using XOR or math formula
            2. Consider using numpy for large grids to improve performance
            3. Add input validation for grid dimensions and value ranges
            4. Consider using Counter from collections for frequency counting
        """
        # Input validation (recommended addition)
        if not grid or len(grid) != len(grid[0]):
            raise ValueError("Grid must be non-empty and square")
            
        # Flatten the grid using zip and find the repeated number by subtracting
        # the sum of unique numbers from the sum of all numbers
        ans = [sum(sum(zip(*grid), ())) - sum(set(sum(zip(*grid), ())))]
        
        # Get the set of all numbers in the grid
        g = set(sum(zip(*grid), ()))
        
        # Calculate total numbers that should be in the grid (n^2)
        n = len(grid[0]) * len(grid[0])
        
        # Find the missing number by checking which number from 1 to n^2
        # is not present in the grid
        for i in range(1, n+1):
            if i not in g:
                ans.append(i)
            
        return ans
        