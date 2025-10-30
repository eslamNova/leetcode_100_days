class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        # print(c)
        for i in range(len(num)):

            n = int(num[i])

            # print(i,n,c[i])

            if c[str(i)] != n:
                return False
        return True
        