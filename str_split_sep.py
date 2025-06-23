class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:

            if separator in w:
                wr = w.split(separator)
                for r in wr:
                    if r:
                        ans.append(r)
            else:
                ans.append(w)
        return ans
        