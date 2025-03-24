"""
Leetcode Problem: Number of Different Integers in a String

Description:
You are given a string word that consists of digits and lowercase English letters.
You need to extract the non-overlapping substrings that represent integers and 
return the number of different integers among them.

Constraints:
- 1 <= word.length <= 1000
- word consists of digits and lowercase English letters
- Leading zeros should be treated as the same integer (e.g., "01" and "1" are the same)

Examples:
- Input: word = "a123bc34d8ef34"
  Output: 3
  Explanation: The integers "123", "34", and "8" are extracted. "34" appears twice but counts once.

- Input: word = "leet1234code234"
  Output: 2
  Explanation: The integers "1234" and "234" are extracted.
"""

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Initialize an empty set to store unique integers
        unique_integers = set()
        
        # Initialize a temporary string to build numbers
        current_num = ""
        
        # Iterate through each character in the word
        for char in word:
            if char.isdigit():
                # If character is a digit, add it to the current number
                current_num += char
            else:
                # If character is not a digit and we have collected a number
                if current_num:
                    # Convert to integer to remove leading zeros and add to set
                    unique_integers.add(int(current_num))
                    # Reset current number
                    current_num = ""
        
        # Check if there's a number at the end of the string
        if current_num:
            unique_integers.add(int(current_num))
        
        # Return the count of unique integers
        return len(unique_integers)


# Optimized solution using regular expressions
import re

class OptimizedSolution:
    def numDifferentIntegers(self, word: str) -> int:
        # Use regex to find all sequences of digits
        # \d+ matches one or more digits
        numbers = re.findall(r'\d+', word)
        
        # Convert each number to integer (removes leading zeros) and store in a set
        unique_integers = {int(num) for num in numbers}
        
        return len(unique_integers)
