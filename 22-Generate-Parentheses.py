class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        ans = [] 

        def gen(oC, cC):

            if oC == cC == n:
                ans.append(\\.join(stack))
                return 
            
            if oC < n:
                stack.append(\(\)
                gen(oC + 1, cC)
                stack.pop()
            
            if cC < oC:
                stack.append(\)\)
                gen(oC, cC + 1)
                stack.pop()
        gen(0,0)
        return ans
        