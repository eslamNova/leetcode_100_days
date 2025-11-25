class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 0

        if k % 2 == 0 and k > 1:
            return -1

        for l in range(1,k+1):
            n = (n * 10 + 1) % k
            if n == 0:
                return l
        # while len(str(n)) <= k:
        #     if n == 0:
        #         return len(str(n))
        #     else:
        #         n = (n * 10 + 1) % k

        return -1
        