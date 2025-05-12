class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        m = 0 
        for n in strs:
            f = False
            for i in n:

                if i.isalpha():
                    f = True
                    if len(n) > m:
                        m = len(n)
                    break
            if not f:
                if int(n) > m:
                    m = int(n)

        return m

                     
