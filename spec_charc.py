class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Count the number of characters that appear in both lowercase and uppercase forms in the given word.
        
        A character is considered 'special' if it appears in both lowercase and uppercase forms.
        For example, in "aBcA", 'a'/'A' is special because it appears in both forms.
        
        Args:
            word: A string containing alphabetic characters
            
        Returns:
            The count of characters that appear in both lowercase and uppercase forms
        """
        # Track unique lowercase and uppercase characters (converted to lowercase for comparison)
        lower_set = set()
        upper_set = set()

        # Iterate through each character in the word
        for char in word:
            if char.islower():
                lower_set.add(char)
            elif char.isupper():
                upper_set.add(char.lower())

        # Return the count of characters that exist in both sets (intersection)
        return len(lower_set & upper_set)

    # Alternative solution with a more efficient single-pass approach
    def numberOfSpecialChars_alt(self, word: str) -> int:
        """
        Alternative implementation using a single set and dictionary to track character occurrences.
        This approach is more memory efficient as it uses a single data structure.
        
        Time Complexity: O(n) where n is the length of the word
        Space Complexity: O(k) where k is the number of unique characters (max 26)
        """
        # Dictionary to track if we've seen both uppercase and lowercase versions
        char_status = {}
        special_count = 0
        
        for char in word:
            lowercase_char = char.lower()
            
            # Initialize status for this character if we haven't seen it before
            if lowercase_char not in char_status:
                char_status[lowercase_char] = {"seen_lower": False, "seen_upper": False}
                
            # Update status based on current character
            if char.islower():
                char_status[lowercase_char]["seen_lower"] = True
            elif char.isupper():
                char_status[lowercase_char]["seen_upper"] = True
                
            # If we've now seen both lowercase and uppercase and haven't counted it yet,
            # increment the counter
            if (char_status[lowercase_char]["seen_lower"] and 
                char_status[lowercase_char]["seen_upper"] and
                char_status[lowercase_char].get("counted", False) == False):
                special_count += 1
                char_status[lowercase_char]["counted"] = True
                
        return special_count


        