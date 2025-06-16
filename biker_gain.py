class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g = [0]

        for n in gain:
            l = g[-1] + n
            g.append(l)
        return max(g)
        