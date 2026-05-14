class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for n in tokens:
            if n in "+-*/":
                if n == "+":
                    a = s.pop()
                    b = s.pop()
                    s.append(a+b)
                elif n == "-":
                    a = s.pop()
                    b = s.pop()
                    s.append(b-a)
                elif n == "*":
                    a = s.pop()
                    b = s.pop()
                    s.append(a*b)
                elif n == "/":
                    a = s.pop()
                    b = s.pop()
                    s.append(int(b/a))

            else:
                s.append(int(n))

        return s.pop()
        
