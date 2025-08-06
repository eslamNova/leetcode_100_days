class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        max_score = -1
        best_divisor = float('inf')

        for di in divisors:
            score = sum(1 for n in nums if n % di == 0)
            if score > max_score or (score == max_score and di < best_divisor):
                max_score = score
                best_divisor = di

        return best_divisor