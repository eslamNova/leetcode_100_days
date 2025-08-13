class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = Counter(s)
        st = Counter(target)
        k = 100
        for n in target:
            if sc[n]//st[n] < k:
                k = sc[n]//st[n]

        return k

        