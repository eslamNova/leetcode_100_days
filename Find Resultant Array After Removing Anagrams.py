"""
Problem: Find Resultant Array After Removing Anagrams

Given an array of strings words, remove all anagrams of the previous word.
An anagram is a word formed by rearranging the letters of a different word.

Example:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation: "baba" and "bbaa" are anagrams of "abba", so they are removed.

Time Complexity: O(N * M) where N is the number of words and M is the average length of a word
Space Complexity: O(N) to store the result array
"""

from collections import Counter
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Removes anagrams from the input array of words.
        
        Args:
            words: A list of strings
            
        Returns:
            A list of strings with anagrams removed
        """
        # Handle edge cases: empty array or single word
        if len(words) <= 1:
            return words
            
        # Initialize with the first word
        current_word = words[0]
        result = []
        
        # Iterate through the words starting from the second word
        for i in range(1, len(words)):
            # Debug print statement - should be removed in production code
            print(words[i])
            
            # Check if current word is an anagram of the previous word
            if Counter(current_word) == Counter(words[i]):
                # If it's the last word and it's an anagram, add the previous word
                if i == len(words) - 1:
                    result.append(current_word)
            else:
                # If not an anagram, add the previous word and update current word
                result.append(current_word)
                current_word = words[i]
                # If it's the last word and not an anagram, add it
                if i == len(words) - 1:
                    result.append(current_word)
                
        return result

# FAANG Interviewer Feedback:
# 1. Good job handling edge cases with the initial check.
# 2. The solution correctly identifies anagrams using Counter.
# 3. Areas for improvement:
#    - Remove debug print statements before submission
#    - Consider using more descriptive variable names (e.g., 'current_word' instead of 's')
#    - The logic for handling the last word is duplicated and could be simplified
#    - Consider adding input validation for empty strings or non-string elements
#    - The solution could be more concise with better control flow
# 4. Alternative approach: You could use a two-pointer technique or a stack-based approach
#    for potentially better readability.
# 5. For production code, consider adding error handling for edge cases.
        