class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        o = 0 

        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
                o += 1
            elif num2 >= num1:
                num2 -= num1
                o += 1
            
        return o
        