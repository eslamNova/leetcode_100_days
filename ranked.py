#O(NLOGN)

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        ranked = {}
        ans = []
        r = 1
        for i in sorted(arr):
            if i not in ranked:
                ranked[i] = r
                r += 1
        for i in arr:
            ans.append(ranked[i])
        return ans
        