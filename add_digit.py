# O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        ans = num
        while len(s) > 1:
            ans = 0

            for n in s:
                ans += int(n)

            s = str(ans)

        return ans
        