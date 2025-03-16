"""
LeetCode Problem 500: Keyboard Row
Description: Given an array of strings words, return the words that can be typed using letters of the alphabet 
on only one row of American keyboard.

In the American keyboard:
- First row: "qwertyuiop"
- Second row: "asdfghjkl"
- Third row: "zxcvbnm"
"""
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Returns words that can be typed using letters from only one row of the American keyboard.
        
        Args:
            words (List[str]): A list of words to check
            
        Returns:
            List[str]: Words that can be typed using only one keyboard row
            
        Complexity Analysis:
            Time Complexity: O(n*m) where n is the number of words and m is the average word length
            Space Complexity: O(n) for storing the result and temporary row mappings
        """
        # Define the three rows of the American keyboard
        r1, r2, r3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        ans = []
        
        for w in words:
            # Track which keyboard row each character belongs to
            wr = []
            for n in w.lower():  # Convert to lowercase for case-insensitive comparison
                if n in r1:
                    wr.append(1)  # First row
                elif n in r2:
                    wr.append(2)  # Second row
                else:
                    wr.append(3)  # Third row (default)

            # If all characters are from the same row (set has only one element)
            if len(set(wr)) == 1:
                ans.append(w)
                
        return ans

# Feedback:
# 1. The solution correctly identifies words that can be typed using only one row of the keyboard.
# 2. Converting words to lowercase is a good approach for case-insensitive matching.
# 3. Using set() to check if all characters are from the same row is efficient.
# 4. Potential improvements:
#    - Could use a dictionary/hash map to map characters to rows for faster lookups
#    - Could handle non-alphabetic characters more explicitly
#    - For very large inputs, could consider using sets instead of strings for row membership checks

# ---------------------------------------------------------------------------------
# OPTIMIZED SOLUTION
# ---------------------------------------------------------------------------------

class OptimizedSolution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Optimized solution using sets and a character-to-row mapping.
        
        Time Complexity: O(n*m) where n is the number of words and m is the average word length
        Space Complexity: O(1) for the row sets (constant) + O(n) for the result
        """
        # Define the three rows as sets for O(1) lookups
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # Pre-compute a mapping of each character to its row
        # This avoids repeated checks for each character
        char_to_row = {}
        for char in row1:
            char_to_row[char] = 1
        for char in row2:
            char_to_row[char] = 2
        for char in row3:
            char_to_row[char] = 3
            
        result = []
        
        for word in words:
            if not word:  # Handle empty string case
                continue
                
            # Get the row of the first character
            first_char_row = char_to_row.get(word[0].lower())
            
            # Check if all characters are in the same row
            if all(char_to_row.get(c.lower()) == first_char_row for c in word):
                result.append(word)
                
        return result

# ---------------------------------------------------------------------------------
# HOW TO ARRIVE AT THE OPTIMIZED SOLUTION
# ---------------------------------------------------------------------------------
# Step 1: Identify the bottlenecks in the original solution
#   - String membership checks (n in r1) are O(k) where k is the length of the string
#   - We're doing these checks for every character in every word
#   - We're building a list of row numbers and then converting to a set

# Step 2: Use sets instead of strings for membership checks
#   - Set membership checks are O(1) on average
#   - This makes checking which row a character belongs to much faster

# Step 3: Pre-compute a character-to-row mapping
#   - Instead of checking each character against each row every time
#   - Build a dictionary that maps each character directly to its row number
#   - This reduces the number of comparisons from 3 to 1 per character

# Step 4: Optimize the "same row" check
#   - Instead of building a list and converting to a set
#   - Check if all characters are in the same row as the first character
#   - Use the 'all()' function with a generator expression for efficiency

# Step 5: Handle edge cases
#   - Empty strings
#   - Non-alphabetic characters (handled by the .get() method with default None)

# The optimized solution improves performance by:
#   1. Reducing the time complexity of row membership checks from O(k) to O(1)
#   2. Eliminating the need to build temporary lists
#   3. Reducing the number of comparisons per character
#   4. Using Python's built-in functions efficiently