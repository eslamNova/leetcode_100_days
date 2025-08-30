class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        n = len(colors)
        ans = 0 
        for i in range(n):

            b = i-1
            f = i + 1

            if b < 0:
                b = n-1
            if f >= n:
                f = 0
            if colors[b] == colors[f]:
                if colors[b] != colors[i]:
                    ans += 1
        return ans