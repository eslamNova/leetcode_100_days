# O(N)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        o_p = deque()
        res = []

        for n in s:
            if n == "(":
                o_p.append(len(res))
            elif n == ")":
                st = o_p.pop()

                res[st:] = res[st:][::-1]
            else:
                res.append(n)
        return "".join(res)
