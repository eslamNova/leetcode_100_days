class Solution:
    """
    A class to solve the problem of splitting a number into two parts to minimize their sum.
    
    Problem Description:
    Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
    1. The concatenation of num1 and num2 is a permutation of num
    2. The sum of num1 and num2 is minimized
    
    Example:
    Input: num = 4325
    Output: 59
    Explanation: We can split 4325 into 43 and 25, and their sum is 68.
    A better split would be 24 and 35, giving us 59.
    """
    
    def splitNum(self, num: int) -> int:
        """
        Splits a number into two parts to minimize their sum.
        
        Args:
            num (int): The input number to be split
            
        Returns:
            int: The minimum possible sum of the two split numbers
            
        Time Complexity: O(n log n) where n is the number of digits
        Space Complexity: O(n) where n is the number of digits
        """
        # Convert number to sorted list of digits
        digits = sorted(list(int(x) for x in str(num)))
        
        # Initialize two empty strings to build our numbers
        num1, num2 = "", ""
        
        # Alternate between adding digits to num1 and num2
        # This ensures we distribute digits evenly and minimize the sum
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)
        
        # Convert strings back to integers and return their sum
        return int(num1) + int(num2)
    
    def splitNum_alternative(self, num: int) -> int:
        """
        Alternative solution using a more concise approach with list comprehension.
        This solution achieves the same result but with cleaner code.
        
        Args:
            num (int): The input number to be split
            
        Returns:
            int: The minimum possible sum of the two split numbers
        """
        # Convert to sorted digits
        digits = sorted(str(num))
        
        # Use list comprehension to split digits into two numbers
        # This is more pythonic and achieves the same result
        num1 = ''.join(digits[::2])  # Take every even-indexed digit
        num2 = ''.join(digits[1::2]) # Take every odd-indexed digit
        
        return int(num1) + int(int(num2) if num2 else 0)

# Example usage and test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [4325, 687, 100, 9999]
    
    for num in test_cases:
        result1 = solution.splitNum(num)
        result2 = solution.splitNum_alternative(num)
        print(f"Input: {num}")
        print(f"Original solution result: {result1}")
        print(f"Alternative solution result: {result2}")
        print(f"Results match: {result1 == result2}\n")
        