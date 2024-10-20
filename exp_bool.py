# O(N)class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char == ',':
                continue  # Ignore commas, they're just separators
            elif char != ')':
                stack.append(char)
            else:
                # We reached a closing parenthesis, now evaluate the sub-expression
                sub_expr = []
                
                # Pop until we find the opening parenthesis
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                
                # Discard the '('
                stack.pop()
                
                # The operator is just before the parenthesis
                operator = stack.pop()
                
                # Evaluate the sub-expression based on the operator
                if operator == '&':
                    # AND operation, all must be true
                    stack.append('t' if all(c == 't' for c in sub_expr) else 'f')
                elif operator == '|':
                    # OR operation, at least one must be true
                    stack.append('t' if any(c == 't' for c in sub_expr) else 'f')
                elif operator == '!':
                    # NOT operation, negate the single sub-expression
                    stack.append('t' if sub_expr[0] == 'f' else 'f')

        # The final result will be the only item left on the stack
        return stack.pop() == 't'

