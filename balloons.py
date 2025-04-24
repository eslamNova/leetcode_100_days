class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        ans = []
        for l in "balon":
            if l == "o":
                ans.append(c[l]//2)
            elif l == "l":
                ans.append(c[l]//2)
            else:
                ans.append(c[l])
        return min(ans)
        