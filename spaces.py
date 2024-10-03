# O(N)
class Solution:
    def reorderSpaces(self, text: str) -> str:

        # Step 1: Split the text into words and count total spaces
        words = text.split()
        total_spaces = len(text) - sum(len(word) for word in words)

        # Step 2: Calculate spaces between words and extra spaces
        if len(words) > 1:
            spaces_between_words = total_spaces // (len(words) - 1)
            extra_spaces = total_spaces % (len(words) - 1)
        else:
            spaces_between_words = 0
            extra_spaces = total_spaces

        # Step 3: Rebuild the string with spaces
        result = (' ' * spaces_between_words).join(words)
        result += ' ' * extra_spaces

        return result