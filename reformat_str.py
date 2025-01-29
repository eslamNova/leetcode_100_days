class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        # Separate letters and digits
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)

        # If the absolute difference in count is more than 1, it's impossible to reformat
        if abs(len(letters) - len(digits)) > 1:
            return ""

        # Ensure letters list is longer or equal for easy merging
        if len(digits) > len(letters):
            letters, digits = digits, letters

        # Interleave letters and digits
        result = []
        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])

        # If letters are more, append the last letter
        if len(letters) > len(digits):
            result.append(letters[-1])

        return "".join(result)
            