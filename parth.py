class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        # st = []
        # valid = False

        # for p,i in zip(s, locked):
        #     if p == "(":
        #         if st == []:
        #             st.append(p)
        #             valid = False
        #         else:
        #             if i == "0":
        #                 st.pop(0)
        #                 valid = True
        #     else:
        #         if st == []:
        #             if i == "0":
        #                 st.append("(")
        #                 valid = False
        #         else:
        #             st.pop(0)
        #             valid = True
            

        # return valid
        # Edge case: If the length of the string is odd, it cannot be balanced.
        if len(s) % 2 != 0:
            return False

        # Initialize counters to track the minimum and maximum number of open parentheses.
        # `min_open` represents the minimum number of '(' we must have.
        # `max_open` represents the maximum number of '(' we can have.
        min_open = 0
        max_open = 0

        # Traverse the string from left to right.
        for i in range(len(s)):
            if locked[i] == '0':
                # If the character is unlocked, it can be either '(' or ')'.
                # So, we adjust `min_open` and `max_open` accordingly.
                min_open -= 1  # Treat it as ')'
                max_open += 1  # Treat it as '('
            else:
                # If the character is locked, we update `min_open` and `max_open` based on the character.
                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                else:
                    min_open -= 1
                    max_open -= 1

            # If `max_open` becomes negative, it means there are more ')' than '(' and we cannot balance it.
            if max_open < 0:
                return False

            # `min_open` cannot be negative because we can always flip unlocked characters to '('.
            # So, we reset it to 0 if it goes below 0.
            if min_open < 0:
                min_open = 0

        # After traversing the string, if `min_open` is 0, it means the string can be balanced.
        return min_open == 0