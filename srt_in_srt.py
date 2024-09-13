# O(N*M)

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        test = set(allowed)
        ans = 0
        add = False

        for w in words:
            add = True
            for a in set(w):
                if a not in test:
                    add = False
                    break
            if add:
                ans += 1
        return ans