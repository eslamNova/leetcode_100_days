#   O(3*2N)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        t = 3 * 2**(n-1)
        result = []

        def backtrack(current_string):
            """
            Recursive function to generate strings.
            
            Arguments:
            current_string (str): The string generated so far.
            """
            # ✅ Base Case: If the string length reaches n, print and store it.
            if len(current_string) == n:
                # print(current_string)  # Print the string
                result.append(current_string)  # Store the string
                return

            # 🔁 Recursive Step: Try each of the letters 'a', 'b', 'c'
            for char in ['a', 'b', 'c']:
                # 🚫 Rule: No two adjacent letters can be the same
                if len(current_string) == 0 or char != current_string[-1]:
                    # 🌱 Choose the character and move forward
                    backtrack(current_string + char)

        # 🚀 Start the recursion with an empty string
        backtrack("")
        if k <= t:
            return result[k-1]
        return ""
        