# O(N∗M)

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mi = []
        ma = []

        for m in matrix:
            mi.append(min(m))

        mat = zip(*matrix)

        for m in mat:
            ma.append(max(m))

        ans = []

        for n in mi:
            if n in ma:
                ans.append(n)
        return ans
        