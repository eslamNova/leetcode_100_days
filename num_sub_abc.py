"""
Author: Islam Ashraf
Problem: Number of Substrings Containing All Three Characters
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Count the number of substrings containing all three characters 'a', 'b', and 'c'.
        
        This solution uses the sliding window technique to efficiently find all valid substrings.
        
        Complexity Analysis:
            Time Complexity: O(n) where n is the length of string s
                - The right pointer moves n times through the string
                - The left pointer can also move up to n times in total
                - Each operation inside the loops is O(1)
                - Total operations: O(n + n) = O(n)
            
            Space Complexity: O(1)
                - We use a dictionary with fixed size (3 keys)
                - Two integer pointers (l and r)
                - One counter variable (o)
                - Space used doesn't grow with input size
        
        Args:
            s (str): Input string containing only characters 'a', 'b', and 'c'
            
        Returns:
            int: Number of substrings that contain at least one of each character 'a', 'b', and 'c'
        """
        # Dictionary to keep track of frequency of each character in current window
        c = {"a": 0, "b": 0, "c": 0}
        
        # Initialize left pointer of sliding window and output counter
        l = 0  # left pointer
        o = 0  # output counter (number of valid substrings)
        
        # Iterate through string using right pointer
        for r in range(len(s)):
            # Add current character to frequency count
            c[s[r]] += 1
            
            # While window contains all three characters
            while c["a"] > 0 and c["b"] > 0 and c["c"] > 0:
                # All substrings starting at l and ending at r or beyond are valid
                # Add count of all such possible substrings
                o += len(s) - r
                
                # Shrink window from left side
                c[s[l]] -= 1  # Remove leftmost character from frequency count
                l += 1        # Move left pointer right
                
        return o  
        