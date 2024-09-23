# O(N)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        st = s1 + " " + s2
        c = Counter(st.split(" "))
        return [t for t in c if c[t] == 1]
    #extra day
        