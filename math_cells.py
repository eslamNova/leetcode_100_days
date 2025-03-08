class Solution:
    def coloredCells(self, n: int) -> int:
        """
        Calculate the number of colored cells after n steps in a grid coloring pattern.
        
        In this problem, we start with a single colored cell at step 1.
        For each subsequent step, we color the cells that share an edge with 
        colored cells from the previous step.
        
        Args:
            n (int): Number of steps, where 1 <= n <= 10^5
            
        Returns:
            int: Total number of colored cells after n steps
            
        Time Complexity: O(n) - We iterate from 2 to n once
        Space Complexity: O(1) - We only use a constant amount of extra space
        """
        # Initialize with 1 colored cell at step 1
        ans = 1 
        
        # Iterate through steps 2 to n
        for i in range(2, n+1):  
            # For each step, we add 4 cells at the corners
            ans += 4
            
            # Starting from step 3, we also add cells along the sides
            # At step i, we add (i-2)*4 cells along the sides
            if i >= 3:
                ans += (i-2) * 4
                
        return ans
        