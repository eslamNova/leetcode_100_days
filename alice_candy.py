class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        no = len(candyType) // 2

        ty = len(set(candyType))

        return min(ty, no)
        