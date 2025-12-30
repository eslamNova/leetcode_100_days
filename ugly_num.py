class Solution:
    def isUgly(self, n: int) -> bool:
        
        for i in range(31):
            for j in range(31):
                for k in range(31):
                    h = (2 ** i)  * (3**j) * (5**k)
                    # print(h)
                    if h == n:
                        return True
                    # if h > n:
                    #     return False
        return False