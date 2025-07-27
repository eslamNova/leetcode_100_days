class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False

        for ch in word:
            # 2. Only digits and English letters
            if not (ch.isdigit() or ch.isalpha()):
                return False

            # 3. Check for vowel or consonant
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        # 4. Must have at least one vowel and one consonant
        return has_vowel and has_consonant
        #
        