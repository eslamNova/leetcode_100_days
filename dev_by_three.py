class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Determines if a given number can be expressed as a sum of distinct powers of three.
        
        Args:
            n (int): A positive integer to check
            
        Returns:
            bool: True if n can be expressed as sum of distinct powers of 3, False otherwise
            
        Example:
            n = 12 = 3^2 + 3^1 = 9 + 3 -> True
            n = 21 = cannot be expressed as sum of distinct powers of 3 -> False
        """
        # The key insight is that when we convert n to base-3,
        # each digit must be 0 or 1 (not 2) for the number to be
        # expressible as a sum of distinct powers of 3
        
        while n > 0:
            # Get the remainder when divided by 3 (the current base-3 digit)
            if n % 3 == 2:
                # If we find a '2' in base-3 representation, it's impossible
                return False
            # Integer divide by 3 to check the next digit
            n //= 3
        return True
        