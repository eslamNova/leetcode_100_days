class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        ans = 0 
        if len(words1) < len(words2):
            for w in c1:
                if c1[w] == 1:
                    if c2[w] == 1:
                        ans += 1
        else:
            for w in c2:
                if c2[w] == 1:
                    if c1[w] == 1:
                        ans += 1
        return ans
        