# O(N)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for n in tokens:
            if n not in "+-*/":
                st.append(int(n))
            else:
                num = st.pop()

                if n == "+":
                    st[-1] += num
                elif n == "-":
                    st[-1] -= num
                elif n == "*":
                    st[-1] *= num
                elif n == "/":
                    st[-1] = int(st[-1]/num)

        return st[0]
        
        