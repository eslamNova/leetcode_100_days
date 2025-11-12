class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        c = Counter(chars)
        a = 0
        for n in words:
            good = True
            m = Counter(n)
            for i in n:
                if i not in chars:
                    good = False
                    break
                else:
                    if m[i] > c[i]:
                        good = False
                        break
            if good:
                a += len(n)

        return a
        