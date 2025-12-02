class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        p = -1
        for n in nums:

            if p == -1:
                if n % 2 == 0 :
                    p = 0
                else:
                    p = 1
            else:
                print(n)
                if p == 0:
                    if n % 2 != 0 and p == 0:
                        p = 1
                    else:
                        print("e1")
                        return False
                else:
                    if n % 2 == 0 and p == 1:
                        p = 0
                    else:
                        print("e2")
                        return False
        return True