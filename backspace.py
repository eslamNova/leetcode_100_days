# O(N)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        st1, st2 = [], []

        for i in range(len(s)):
            
            if s[i] != "#":
                st1.append(s[i])
            else:
                if st1:
                    st1.pop()

        for i in range(len(t)):

            if t[i] != "#":
                st2.append(t[i])
            else:
                if st2:
                    st2.pop()
        return st1 == st2

        
        