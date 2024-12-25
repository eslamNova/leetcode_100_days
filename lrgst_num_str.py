# O(NlogN)
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()  # Using a set to store unique digits
        
        for char in s:
            if char.isdigit():  # Check if the character is a digit
                digits.add(int(char))  # Add the digit to the set
        
        if len(digits) < 2:
            return -1  # Return -1 if there are less than 2 unique digits
        
        # Sort the digits in descending order and return the second largest
        sorted_digits = sorted(digits, reverse=True)
        return sorted_digits[1]
        