class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ord = ord(target)
        smallest_greater = None

        for ch in letters:
            if ord(ch) > target_ord:
                if smallest_greater is None or ord(ch) < ord(smallest_greater):
                    smallest_greater = ch

        return smallest_greater if smallest_greater else letters[0]
        