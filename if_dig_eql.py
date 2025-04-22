"""
Problem: Check if a string of digits can be reduced to a string with equal digits
         by repeatedly adding adjacent digits modulo 10.

Analysis:
- The algorithm repeatedly processes the string by adding adjacent digits modulo 10
- This continues until the string length is reduced to 2
- If the final two digits are equal, return True; otherwise, return False
- Time Complexity: O(n²) where n is the length of the input string
- Space Complexity: O(n) for storing intermediate results

Example:
Input: "1234"
Process:
1. "1234" -> "357" (1+2=3, 2+3=5, 3+4=7)
2. "357" -> "82" (3+5=8, 5+7=12%10=2)
3. "82" -> "8" and "2" are not equal, so return False

Input: "12345"
Process:
1. "12345" -> "3579" (1+2=3, 2+3=5, 3+4=7, 4+5=9)
2. "3579" -> "826" (3+5=8, 5+7=12%10=2, 7+9=16%10=6)
3. "826" -> "08" (8+2=10%10=0, 2+6=8)
4. "08" -> "0" and "8" are not equal, so return False
"""

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Determines if a string of digits can be reduced to a string with equal digits
        by repeatedly adding adjacent digits modulo 10.
        
        Args:
            s (str): A string of digits
            
        Returns:
            bool: True if the string can be reduced to equal digits, False otherwise
            
        Example:
            >>> solution = Solution()
            >>> solution.hasSameDigits("1234")
            False
            >>> solution.hasSameDigits("12345")
            False
        """
        # Continue processing until the string length is reduced to 2
        while len(s) > 2:
            ss = ""
            # Process each pair of adjacent digits
            for i in range(len(s)-1):
                # Add adjacent digits and take modulo 10
                t = (int(s[i]) + int(s[i+1])) % 10
                # Append the result to the new string
                ss += str(t)
            # Update the string for the next iteration
            s = ss
        
        # Check if the final two digits are equal
        if s[0] == s[1]:
            return True
        return False
        