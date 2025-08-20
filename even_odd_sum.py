class Solution:
    def isBalanced(self, num: str) -> bool:
        sa , sb = 0,0
        f = True
        for i in num:
            if f:
                f = False
                sa += int(i)
            else:
                f = True
                sb += int(i)

        return sa == sb
        