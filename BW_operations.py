class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        ans = 100

        for i in range(len(blocks)-k+1):
            t = Counter(blocks[i:i+k])
            if t["W"] < ans:
                ans = t["W"]

        return ans