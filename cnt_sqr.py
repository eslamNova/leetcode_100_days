class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n):
            for j in range(1,n):

                x = sqrt(i ** 2 + j ** 2)
                if x.is_integer() and x <= n:
                    ans += 1

        return ans
        