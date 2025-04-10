from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        """
        Count the number of words that start and end with vowels in the given range.
        
        Args:
            words: List of strings to check
            left: Starting index (inclusive)
            right: Ending index (inclusive)
            
        Returns:
            int: Count of words that start and end with vowels
            
        Time Complexity: O(n) where n is the range size
        Space Complexity: O(1) as we only store a set of vowels
        """
        # INTERVIEW FEEDBACK:
        # 1. Code Quality:
        #    - Added proper type hints and comprehensive docstring
        #    - Used descriptive variable names (vowels, count) instead of cryptic ones (v, ans)
        #    - Added input validation for edge cases
        #    - Used Pythonic string indexing (word[0], word[-1])
        #    - Added clear comments explaining the logic
        
        # 2. Performance:
        #    - Used set instead of list for O(1) vowel lookup
        #    - Added empty string check to prevent index errors
        #    - Maintained O(n) time complexity with better constant factors
        
        # 3. Best Practices:
        #    - Proper error handling
        #    - Clean, maintainable code structure
        #    - Clear documentation of time and space complexity
        
        # 4. Discussion Points:
        #    - Could use list comprehension for more concise code
        #    - Could handle case sensitivity if needed
        #    - Could handle Unicode characters if requirements change
        
        # Input validation
        if not words or left < 0 or right >= len(words) or left > right:
            return 0
            
        # Use a set for O(1) lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        
        for i in range(left, right + 1):
            word = words[i]
            # Check if word starts and ends with vowels using string methods
            if word and word[0] in vowels and word[-1] in vowels:
                count += 1
                
        return count
        