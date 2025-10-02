class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                ans[i] = True
        return ans        