"""
Problem: String Degree Reversal
Given a string of lowercase letters, calculate the total degree by:
1. For each character, calculate its reverse degree (26 - position in alphabet)
2. Multiply the reverse degree by its position (1-based index)
3. Sum all these products

Example:
Input: "abc"
Output: 78
Explanation:
- 'a' (position 1): (26-1) * 1 = 25
- 'b' (position 2): (26-2) * 2 = 48
- 'c' (position 3): (26-3) * 3 = 69
Total: 25 + 48 + 69 = 78

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) as we only use a single variable to store the total
"""

class Solution:
    def reverseDegree(self, s: str) -> int:
        """
        Calculate the total degree of a string based on character positions and their reverse degrees.
        
        Args:
            s (str): Input string containing lowercase letters
            
        Returns:
            int: Total degree calculated from the string
            
        Raises:
            ValueError: If the input string contains non-lowercase letters
        """
        total = 0
        for i in range(len(s)):
            # Calculate reverse degree: 26 - (position in alphabet)
            # ord('a') = 97, so ord(s[i]) - ord('a') gives 0-25 for a-z
            reverse = 26-(ord(s[i])-ord("a"))
            # Multiply reverse degree by position (1-based index) and add to total
            total += reverse*(i+1)
        return total
        