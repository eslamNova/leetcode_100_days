class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(100):
            if n == 2 ** i:
                # print(n, 2**i)
                return True
        return False

        