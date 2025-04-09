from difflib import SequenceMatcher

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        w = ""
        for l in licensePlate:
            if l.isalpha():
                w += l.lower()
        # print(w)

        wc = Counter(w)
        ans = None

        for word in words:
            word_counter = Counter(word.lower())
            # Check if word has all required letters in required frequency
            if all(word_counter[ch] >= wc[ch] for ch in wc):
                if ans is None or len(word) < len(ans):
                    ans = word

        return ans
        