class Solution:
    def pivotInteger(self, n: int) -> int:


        x =0 
        a = [j for j in range(1,n+1)]
        if n == 1:
            return n
        # print(a)

        for i in range(n):
            a1 = sum(a[:i])
            # print(a[:i])
            # print(a[i-1:])
            a2 = sum(a[i-1:])
            # print(a1,a2)
            if a1 == a2:
                return i
        return -1
        