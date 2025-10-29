class Solution:
    def smallestNumber(self, n: int) -> int:

        for i in range(0,50,1):
            if 2 ** i > n:
                return 2 ** i - 1
        